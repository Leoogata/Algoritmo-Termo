import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def exibir_boas_vindas():
    print("=" * 50)
    print("Bem-vindo ao Termo Solver!".center(50))
    print("=" * 50)
    print("\nModos disponíveis:")
    print("1 - Termo (1 palavra)")
    print("2 - Dueto (2 palavras)")
    print("3 - Quarteto (4 palavras)")
    print("4 - Jogar os três modos em sequência")
    print("0 - Sair")
    print("=" * 50)
    print("By: Leonardo Ogata".center(50))
    print("=" * 50)

def executar_script(nome_script):
    caminho = os.path.join(BASE_DIR, "algoritmo", nome_script)
    with open(caminho, encoding="utf-8") as f:
        exec(f.read(), globals())

def menu():
    while True:
        exibir_boas_vindas()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            executar_script("termo.py")
        elif escolha == '2':
            executar_script("dueto.py")
        elif escolha == '3':
            executar_script("quarteto.py")
        elif escolha == '4':
            executar_script("termo.py")
            executar_script("dueto.py")
            executar_script("quarteto.py")
        elif escolha == '0':
            print("Até a próxima!")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
