import pandas as pd

# Carrega o dataset de palavras filtradas com frequência de uso
df = pd.read_csv("dados/palavras_filtradas.csv")

def termoSolver(df, i):
    """
    Função recursiva que sugere palavras com base no feedback do jogador.
    
    Parâmetros:
        df (DataFrame): Lista de palavras possíveis com frequência.
        i (int): Número da tentativa atual.
    """
    # Condição de derrota após 6 tentativas
    if i > 5:
        print("\n" + "=" * 50)
        print("  Você perdeu o termo :(".center(50))   
        print("=" * 50)
        return

    # Entrada e validação da palavra tentada
    while True:
        word = input("Digite a palavra que você inseriu: ").strip().lower()
        if len(word) != 5:
            print("Insira uma palavra válida")
        else:
            break

    # Entrada e validação do padrão de cores (C, A, V)
    while True:    
        ans = input("Agora digite o resultado utilizando o formato CAV: ")
        ans = ans.upper().replace(" ", "")
        if len(ans) != 5 or any(letra not in {'C', 'A', 'V'} for letra in ans):
            print("Insira uma entrada válida")
        else:
            break

    # Condição de vitória
    if ans == "VVVVV":
        print("\n" + "=" * 50)
        print("  Parabéns você resolveu o termo!".center(50))   
        print("=" * 50)
        return

    # Filtra as palavras com base no feedback
    # 1. Letras verdes: mesma letra na mesma posição
    for idx in range(len(ans)):
        if ans[idx] == 'V':
            df = df[df['words'].str[idx] == word[idx]]

    # 2. Letras amarelas: letra existe mas em outra posição
    for idx in range(len(ans)):
        if ans[idx] == 'A':
            df = df[df['words'].str.contains(word[idx]) & (df['words'].str[idx] != word[idx])]

    # 3. Letras cinzas: letra não existe (ou restrições em casos com múltiplas ocorrências)
    for idx in range(len(ans)):
        if ans[idx] == 'C':
            # Se for ocorrência única ou não houver outras posições com A/V
            if word.count(word[idx]) == 1 or \
               not any(ans[j] in ('A', 'V') for j in range(len(ans)) if word[j] == word[idx] and j != idx):
                df = df[~df['words'].str.contains(word[idx])]
            else:
                # Remove apenas palavras com essa letra nesta posição específica
                df = df[df['words'].str[idx] != word[idx]]
    
    # Exibe as 5 palavras mais prováveis
    print("\nEssas são as 5 palavras que recomendamos você utilizar: ")
    for counter, (_, row) in enumerate(df.head(5).iterrows(), start=1):
        percentage = (row['frequency'] / df['frequency'].sum()) * 100
        print(f"{counter}. {row['words']} ({int(percentage * 100) / 100}%)")

    # Chamada recursiva para a próxima tentativa
    termoSolver(df, i + 1)

def termoIntro():
    """Exibe as instruções do jogo Termo Solver."""
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

# Fluxo principal
termoIntro()
termoSolver(df, 0)
