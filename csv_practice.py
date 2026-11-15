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

print('Exersise 5:')

original_count = 0
written_count = 0

with open(sales, "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)

with open('data/cleaned.csv', "w", newline="") as cleaned_file:
      writer = csv.writer(cleaned_file)
      writer.writerow(['product', 'price', 'quantity', 'total_revenue'])


for row in reader:
    original_count += 1
    product = row[0]
    price = float(row[1])
    quantity = int(row[2])
    revenue = price * quantity

    if revenue > 100:
        writer.writerow([product, price, quantity, revenue])
        written_count += 1

print(f'Original Count: {original_count}')
print(f'Written Count: {written_count}')
