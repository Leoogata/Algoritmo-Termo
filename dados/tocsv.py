import csv
import sys

# Increase CSV field size limit
csv.field_size_limit(sys.maxsize)

# Input and output file paths
input_file = './dados/palavras.txt'
output_file = './dados/palavras.csv'

# Open the txt file using the correct encoding
with open(input_file, mode='r', encoding='latin1') as txt_file:
    reader = csv.reader(txt_file, delimiter=',')  # Use comma as delimiter

    # Write to CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for row in reader:
            writer.writerow(row)

print("Conversion completed successfully!")
