import pandas as pd

dfBase = pd.read_csv("dados/palavras_filtradas.csv")

dfWord1 = dfBase.copy()
dfWord2 = dfBase.copy()

word1 = False
word2 = False

def process_feedback(df, word, ans):
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
    return df

def duetoSolver(df1, df2, i: int, word1: bool, word2: bool):
    while True:
        word = (str(input("Digite a palavra que você inseriu: ")))
        if len(word) != 5:
            print("Insira uma palavra válida")
        else:
            break
    
    if not word1:
        while True:    
            ans1 = (str(input("Agora digite o resultado da primeira palavra utilizando o formato CAV: ")))
            ans1 = ans1.upper().replace(" ", "")

            if len(ans1) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans1):
                print("Insira um resultado válido")
            else:
                break

        if ans1 == "VVVVV":
            word1 = True 
        else:
            df1 = process_feedback(df1, word, ans1)
    
    if not word2:
        while True:    
            ans2 = (str(input("Agora digite o resultado da segunda palavra utilizando o formato CAV: ")))
            ans2 = ans2.upper().replace(" ", "")

            if len(ans2) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans2):
                print("Insira um resultado válido")
            else:
                break

        if ans2 == "VVVVV":
            word2 = True     
        else:
            df2 = process_feedback(df2, word, ans2)

    if word1 and word2:
        print("\n" + "=" * 50)
        print("  Parabéns você resolveu o dueto!".center(50))   
        print("=" * 50)
        return
    
    if not word1:
        print("\nEssas são as 5 palavras que recomendamos para a palavra 1: ")
        counter = 1  
        for _, row in df1.head(5).iterrows():
            percentage = (row['frequency'] / df1['frequency'].sum()) * 100
            print(f"{counter}. {row['words']} ({percentage:.2f}%)")
            counter += 1

    if not word2:
        print("\nEssas são as 5 palavras que recomendamos para a palavra 2: ")
        counter = 1  
        for _, row in df2.head(5).iterrows():
            percentage = (row['frequency'] / df2['frequency'].sum()) * 100
            print(f"{counter}. {row['words']} ({percentage:.2f}%)")
            counter += 1

    duetoSolver(df1, df2, i + 1, word1, word2)

def duetoIntro():
    print("=" * 50)
    print("  Dueto Solver".center(50))
    print("=" * 50)
    
    print("\nPara jogar a cada palavra inserida você deve retornar o resultado para as duas palavras utilizando as seguintes letras: \n")
    print("  C - Cinza (A palavra não contém essa letra)")
    print("  A - Amarelo (A palavra contém essa letra em outra posição)")
    print("  V - Verde (A palavra contém essa letra nessa posição)")
    
    print("\n" + "=" * 50)
    print("  Vamos começar!".center(50))
    print("  DICA: Recomendamos FORTEMENTE que comece com as palavras 'seria' e 'mundo'.")
    print("=" * 50)

duetoIntro()
duetoSolver(dfWord1, dfWord2, 0, word1, word2)