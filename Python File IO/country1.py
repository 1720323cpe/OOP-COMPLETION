import csv

with open('countries.csv', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)