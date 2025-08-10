import pandas as pd

# Carrega dataset base com palavras e suas frequências
dfBase = pd.read_csv("dados/palavras_filtradas.csv")

# Criamos cópias independentes para as 4 palavras do quarteto
dfWord1 = dfBase.copy()
dfWord2 = dfBase.copy()
dfWord3 = dfBase.copy()
dfWord4 = dfBase.copy()

# Flags para controlar se cada palavra já foi resolvida
word1 = False
word2 = False
word3 = False
word4 = False

def process_feedback(df, word, ans):
    """
    Filtra o DataFrame com base no feedback do usuário para uma palavra:
    - V (Verde): letra correta na posição correta
    - A (Amarelo): letra presente em outra posição
    - C (Cinza): letra ausente, considerando letras repetidas

    Retorna o DataFrame filtrado.
    """
    # Letras verdes: fixam a letra na posição correta
    for i in range(len(ans)):
        if ans[i] == 'V':
            df = df[df['words'].str[i] == word[i]]

    # Letras amarelas: letra existe, mas não naquela posição
    for i in range(len(ans)):
        if ans[i] == 'A':
            df = df[df['words'].str.contains(word[i]) & (df['words'].str[i] != word[i])]

    # Letras cinzas: letra não existe, exceto se houver outras ocorrências com status diferente
    for i in range(len(ans)):
        if ans[i] == 'C':
            if word.count(word[i]) == 1 or \
               not any(ans[j] in ('A', 'V') for j in range(len(ans)) if word[j] == word[i] and j != i):
                df = df[~df['words'].str.contains(word[i])]
            else:
                df = df[df['words'].str[i] != word[i]]
    return df

def quartetoSolver(df1, df2, df3, df4, i: int, word1: bool, word2: bool, word3: bool, word4: bool):
    """
    Função recursiva que gerencia o fluxo do jogo Quarteto,
    solicitando inputs do usuário e filtrando possíveis palavras para cada palavra-alvo.

    Parâmetros:
        df1, df2, df3, df4: DataFrames filtrados para cada palavra
        i: índice da tentativa atual
        word1, word2, word3, word4: flags indicando se as palavras já foram descobertas
    """
    # Condição de derrota após 9 tentativas
    if i > 8:
        print("\n" + "=" * 50)
        print("  Você perdeu o dueto :(".center(50))   
        print("=" * 50)
        return
    
    # Entrada válida da palavra tentada pelo usuário
    while True:
        word = input("Digite a palavra que você inseriu: ").strip().lower()
        if len(word) != 5:
            print("Insira uma palavra válida")
        else:
            break

    # Processa o feedback para cada palavra se ainda não resolvida
    if not word1:
        while True:
            ans1 = input("Agora digite o resultado da primeira palavra utilizando o formato CAV: ").upper().replace(" ", "")
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
            ans2 = input("Agora digite o resultado da segunda palavra utilizando o formato CAV: ").upper().replace(" ", "")
            if len(ans2) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans2):
                print("Insira um resultado válido")
            else:
                break
        if ans2 == "VVVVV":
            word2 = True
        else:
            df2 = process_feedback(df2, word, ans2)

    if not word3:
        while True:
            ans3 = input("Agora digite o resultado da terceira palavra utilizando o formato CAV: ").upper().replace(" ", "")
            if len(ans3) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans3):
                print("Insira um resultado válido")
            else:
                break
        if ans3 == "VVVVV":
            word3 = True
        else:
            df3 = process_feedback(df3, word, ans3)

    if not word4:
        while True:
            ans4 = input("Agora digite o resultado da quarta palavra utilizando o formato CAV: ").upper().replace(" ", "")
            if len(ans4) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans4):
                print("Insira um resultado válido")
            else:
                break
        if ans4 == "VVVVV":
            word4 = True
        else:
            df4 = process_feedback(df4, word, ans4)

    # Verifica se todas as palavras já foram descobertas
    if word1 and word2 and word3 and word4:
        print("\n" + "=" * 50)
        print("  Parabéns você resolveu o quarteto!".center(50))
        print("=" * 50)
        return

    # Exibe sugestões para cada palavra ainda não resolvida
    if not word1:
        print("\nEssas são as 5 palavras que recomendamos para a palavra 1: ")
        for idx, (_, row) in enumerate(df1.head(5).iterrows(), start=1):
            percentage = (row['frequency'] / df1['frequency'].sum()) * 100
            print(f"{idx}. {row['words']} ({percentage:.2f}%)")

    if not word2:
        print("\nEssas são as 5 palavras que recomendamos para a palavra 2: ")
        for idx, (_, row) in enumerate(df2.head(5).iterrows(), start=1):
            percentage = (row['frequency'] / df2['frequency'].sum()) * 100
            print(f"{idx}. {row['words']} ({percentage:.2f}%)")

    if not word3:
        print("\nEssas são as 5 palavras que recomendamos para a palavra 3: ")
        for idx, (_, row) in enumerate(df3.head(5).iterrows(), start=1):
            percentage = (row['frequency'] / df3['frequency'].sum()) * 100
            print(f"{idx}. {row['words']} ({percentage:.2f}%)")

    if not word4:
        print("\nEssas são as 5 palavras que recomendamos para a palavra 4: ")
        for idx, (_, row) in enumerate(df4.head(5).iterrows(), start=1):
            percentage = (row['frequency'] / df4['frequency'].sum()) * 100
            print(f"{idx}. {row['words']} ({percentage:.2f}%)")

    # Continua para a próxima tentativa
    quartetoSolver(df1, df2, df3, df4, i + 1, word1, word2, word3, word4)

def quartetoIntro():
    """Exibe instruções para o modo Quarteto."""
    print("=" * 50)
    print("  Quarteto Solver".center(50))
    print("=" * 50)

    print("\nPara jogar, a cada palavra inserida você deve retornar o resultado para as quatro palavras utilizando as seguintes letras: \n")
    print("  C - Cinza (A palavra não contém essa letra)")
    print("  A - Amarelo (A palavra contém essa letra em outra posição)")
    print("  V - Verde (A palavra contém essa letra nessa posição)")

    print("\n" + "=" * 50)
    print("  Vamos começar!".center(50))
    print("  DICA: Recomendamos FORTEMENTE que comece com as palavras 'seria', 'mundo'.")
    print("=" * 50)

# Inicializa o jogo Quarteto
quartetoIntro()
quartetoSolver(dfWord1, dfWord2, dfWord3, dfWord4, 0, word1, word2, word3, word4)
