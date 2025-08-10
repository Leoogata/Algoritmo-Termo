import csv
import re

input_file = './dados/palavras.txt'
output_file = './dados/palavras.csv'

# Expressão regular para linhas no formato:
# número(s) seguido de espaço(s), depois qualquer sequência de caracteres (token)
pattern = re.compile(r'^(\d+)\s+(.*)$')

# Abre arquivo de entrada com encoding latin-1 e arquivo de saída CSV em utf-8
with open(input_file, 'r', encoding='latin-1') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:

    writer = csv.writer(outfile)
    writer.writerow(['count', 'token'])  # Cabeçalho do CSV

    total = 0      # Contador de linhas processadas com sucesso
    skipped = 0    # Contador de linhas ignoradas por formato inválido

    # Percorre cada linha do arquivo de entrada, numerando para debug
    for line_num, line in enumerate(infile, start=1):
        stripped = line.strip()
        if not stripped:
            continue  # Ignora linhas vazias

        match = pattern.match(stripped)
        if not match:
            print(f"⚠️ Skipped line {line_num}: {stripped}")  # Log de linhas mal formatadas
            skipped += 1
            continue

        count, token = match.groups()
        writer.writerow([count, token])  # Escreve linha formatada no CSV
        total += 1

print(f"✅ Done! Parsed {total} lines. Skipped {skipped} malformed lines.")