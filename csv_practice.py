print('Self Reflection:')

#1.

#2.

#3.

import csv
from datetime import datetime

print('Exersise 1:')

sales = "data/sales.csv"

print('Exersise 2:')

with open(sales, "r", newline="") as sales:
    reader = csv.reader(sales)

    for row in reader:
        print(row)
