import csv

with open("Book1.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    writer = csv.writer(new_csv)
    print("Processing...")



