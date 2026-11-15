print('Self Reflection:')

#1.

#2.

#3.

import csv
from datetime import datetime

print('Exersise 1:')

sales = "data/sales.csv"

print('Exersise 2:')

with open(sales, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

print('Exersise 3:')

with open(sales, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(header)

    for row in reader:
        print(row)