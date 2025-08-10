import pandas as pd
from unidecode import unidecode

# Carrega o CSV ignorando linhas com erros de formatação
df = pd.read_csv('./dados/palavras.csv', on_bad_lines='skip')

# Ajusta nomes das colunas para padrão utilizado no projeto
df.columns = ['frequency', 'words']

# Filtra para manter somente palavras com exatamente 5 letras
df = df[df['words'].str.len() == 5]

# Remove acentuação para padronização
df['words'] = df['words'].apply(unidecode)

# Converte todas as palavras para minúsculas para uniformidade
df['words'] = df['words'].str.lower()

# Remove palavras duplicadas, mantendo apenas a primeira ocorrência
df = df.drop_duplicates(subset='words')

# Salva o resultado limpo em novo arquivo CSV, sem índice
df.to_csv('./dados/palavras_filtradas.csv', index=False)
