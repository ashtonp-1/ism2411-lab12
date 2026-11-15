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

print('Exersise 4:')

total_revenue = 0

with open(sales, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    print(header)

    for row in reader:
       product = row[0]
       price = float(row[1])
       quantity = int(row[2])
       revenue = price * quantity
       total_revenue += revenue

print(f'Total Revenue: ${total_revenue:.2f}')
