import pandas as pd

# Carrega o dataset base de palavras com frequência
dfBase = pd.read_csv("dados/palavras_filtradas.csv")

# Cópias independentes para os dois conjuntos de palavras
dfWord1 = dfBase.copy()
dfWord2 = dfBase.copy()

# Flags para controle de palavras resolvidas
word1 = False
word2 = False

def process_feedback(df, word, ans):
    """
    Filtra o DataFrame com base no feedback (ans) recebido para uma palavra.

    Verde (V): letra correta na posição correta.
    Amarelo (A): letra presente, mas em outra posição.
    Cinza (C): letra ausente, ou tratamento especial para letras repetidas.

    Retorna o DataFrame filtrado.
    """
    for i in range(len(ans)):
        if ans[i] == 'V':
            df = df[df['words'].str[i] == word[i]]

    for i in range(len(ans)):
        if ans[i] == 'A':
            df = df[df['words'].str.contains(word[i]) & (df['words'].str[i] != word[i])]

    for i in range(len(ans)):
        if ans[i] == 'C':
            if word.count(word[i]) == 1 or \
               not any(ans[j] in ('A', 'V') for j in range(len(ans)) if word[j] == word[i] and j != i):
                df = df[~df['words'].str.contains(word[i])]
            else:
                df = df[df['words'].str[i] != word[i]]
    return df

def duetoSolver(df1, df2, i: int, word1: bool, word2: bool):
    """
    Função recursiva que gerencia o jogo Dueto, permitindo que o usuário
    insira uma palavra e seus respectivos feedbacks para as duas palavras-alvo.

    Parâmetros:
        df1, df2: DataFrames filtrados para as duas palavras.
        i: Tentativa atual.
        word1, word2: Flags indicando se as palavras já foram resolvidas.
    """
    # Condição de derrota após 7 tentativas
    if i > 6:
        print("\n" + "=" * 50)
        print("  Você perdeu o dueto :(".center(50))   
        print("=" * 50)
        return
    
    # Validação da palavra inserida pelo usuário
    while True:
        word = input("Digite a palavra que você inseriu: ").strip().lower()
        if len(word) != 5:
            print("Insira uma palavra válida")
        else:
            break
    
    # Feedback para a primeira palavra, se ainda não resolvida
    if not word1:
        while True:
            ans1 = input("Agora digite o resultado da primeira palavra utilizando o formato CAV: ")
            ans1 = ans1.upper().replace(" ", "")
            if len(ans1) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans1):
                print("Insira um resultado válido")
            else:
                break

        if ans1 == "VVVVV":
            word1 = True
        else:
            df1 = process_feedback(df1, word, ans1)

    # Feedback para a segunda palavra, se ainda não resolvida
    if not word2:
        while True:
            ans2 = input("Agora digite o resultado da segunda palavra utilizando o formato CAV: ")
            ans2 = ans2.upper().replace(" ", "")
            if len(ans2) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans2):
                print("Insira um resultado válido")
            else:
                break

        if ans2 == "VVVVV":
            word2 = True
        else:
            df2 = process_feedback(df2, word, ans2)

    # Condição de vitória para ambas as palavras
    if word1 and word2:
        print("\n" + "=" * 50)
        print("  Parabéns você resolveu o dueto!".center(50))
        print("=" * 50)
        return

    # Exibe sugestões para as palavras ainda não resolvidas
    if not word1:
        print("\nEssas são as 5 palavras que recomendamos para a palavra 1: ")
        for counter, (_, row) in enumerate(df1.head(5).iterrows(), start=1):
            percentage = (row['frequency'] / df1['frequency'].sum()) * 100
            print(f"{counter}. {row['words']} ({percentage:.2f}%)")

    if not word2:
        print("\nEssas são as 5 palavras que recomendamos para a palavra 2: ")
        for counter, (_, row) in enumerate(df2.head(5).iterrows(), start=1):
            percentage = (row['frequency'] / df2['frequency'].sum()) * 100
            print(f"{counter}. {row['words']} ({percentage:.2f}%)")

    # Chamada recursiva para próxima tentativa
    duetoSolver(df1, df2, i + 1, word1, word2)

def duetoIntro():
    """Exibe as instruções para o modo Dueto."""
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

# Início do jogo
duetoIntro()
duetoSolver(dfWord1, dfWord2, 0, word1, word2)
