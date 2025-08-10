# Termo Solver

**Termo** é um jogo de palavras semelhante a jogos de adivinhação como Wordle, onde o objetivo é descobrir palavras de 5 letras com base em feedback sobre as letras corretas, letras na posição errada e letras ausentes.

## Sobre o Algoritmo

Este projeto contém algoritmos para auxiliar na resolução do jogo Termo, incluindo modos para uma palavra (Termo), dois (Dueto) e quatro palavras (Quarteto). O algoritmo recebe as palavras inseridas e o feedback do jogo, e filtra uma lista de palavras recomendadas para facilitar a próxima tentativa.

## Como Rodar

1. Certifique-se de ter o Python 3 instalado e as bibliotecas necessárias (`pandas`, `unidecode`).
2. Prepare o arquivo `palavras_filtradas.csv` com a lista de palavras filtradas (gerado a partir do script de limpeza).
3. Execute o arquivo principal `main.py`:
   ```bash
   python main.py
   ```
4. Após rodar `main.py`, você poderá escolher pelo console qual modo deseja jogar:
   - **1** - Termo (1 palavra)
   - **2** - Dueto (2 palavras)
   - **3** - Quarteto (4 palavras)
   - **4** - Jogar os três modos em sequência
   - **0** - Sair

5. Siga as instruções na tela para inserir as palavras tentadas e o feedback no formato:

   - `C` para Cinza: a letra **não existe** na palavra.
   - `A` para Amarelo: a letra existe na palavra, **mas não na posição indicada**.
   - `V` para Verde: a letra está na **posição correta**.

### Exemplo de como inserir o feedback no formato CAV

Após tentar uma palavra no jogo, você receberá um feedback visual indicando quais letras estão corretas, quais estão na palavra mas na posição errada, e quais não existem na palavra.

Você deve transcrever esse feedback para o console usando as letras:

- **V** para Verde (letra correta na posição correta),
- **A** para Amarelo (letra está na palavra, mas em outra posição),
- **C** para Cinza (letra não está na palavra).

Por exemplo, suponha que você tentou a palavra **"mundo"** e o jogo indicou o seguinte feedback:

| Letra | m | u | n | d | o |
|-------|---|---|---|---|---|
| Status| Cinza | Verde | Amarelo | Cinza | Cinza |

Você deve então digitar no console:

```
CVACC
```

Esse é o formato que o algoritmo espera para processar o feedback e filtrar as próximas palavras recomendadas.

## Desenvolvido por

Leonardo Ogata Pedrosa
