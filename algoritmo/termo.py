import pandas as pd

df = pd.read_csv("dados/palavras_filtradas.csv")

def termoSolver(df, i):
    if i > 5:
        print("\n" + "=" * 50)
        print("  Você perdeu o termo :(".center(50))   
        print("=" * 50)
        return

    while True:
        word = (str(input("Digite a palavra que você inseriu: ")))
        if len(word) != 5:
            print("Insira uma palavra válida")
        else:
            break

    while True:    
        ans = (str(input("Agora digite o resultado utilizando o formato CAV: ")))
        ans = ans.upper().replace(" ", "")

        if len(ans) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans):
            print("Insira uma palavra válida")
        else:
            break

    if ans == "VVVVV":
        print("\n" + "=" * 50)
        print("  Parabéns você resolveu o termo!".center(50))   
        print("=" * 50)
        return

    # Primeiro processamos as letras verdes
    for i in range(len(ans)):
        if ans[i] == 'V':
            df = df[df['words'].str[i] == word[i]]

    # Depois processamos as letras amarelas
    for i in range(len(ans)):
        if ans[i] == 'A':
            # A letra existe na palavra mas não nesta posição
            df = df[df['words'].str.contains(word[i]) & (df['words'].str[i] != word[i])]

    # Finalmente processamos as letras cinzas
    for i in range(len(ans)):
        if ans[i] == 'C':
            # Verifica se esta letra não aparece em outras posições com status diferente
            if word.count(word[i]) == 1 or \
               not any(ans[j] in ('A', 'V') for j in range(len(ans)) if word[j] == word[i] and j != i):
                # Se é a única ocorrência ou não há outras ocorrências com status diferente
                df = df[~df['words'].str.contains(word[i])]
            else:
                # Se há outras ocorrências com status diferente, só remove desta posição específica
                df = df[df['words'].str[i] != word[i]]
    
    print("\nEssas são as 5 palavras que recomendamos você utilizar: ")
    counter = 1  
    for _, row in df.head(5).iterrows():
        percentage = (row['frequency'] / df['frequency'].sum()) * 100
        print(f"{counter}. {row['words']} ({int(percentage * 100) / 100}%)")
        counter += 1

    termoSolver(df, i + 1)

def termoIntro():
    print("=" * 50)
    print("  Termo Solver".center(50))
    print("=" * 50)
    
    print("\nPara jogar, a cada palavra inserida, você deve retornar o resultado utilizando as seguintes letras: \n")
    print("  C - Cinza (A palavra não contém essa letra)")
    print("  A - Amarelo (A palavra contém essa letra em outra posição)")
    print("  V - Verde (A palavra contém essa letra nessa posição)")
    
    print("\n" + "=" * 50)
    print("  Vamos começar!".center(50))
    print("  DICA: Recomendamos FORTEMENTE que comece com as palavras 'seria' e 'mundo'.")
    print("=" * 50)

termoIntro()
termoSolver(df, 0)


