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


print('Exersise 5:')

original_count = 0
written_count = 0

with open(sales, "r", newline="") as infile:
    reader = csv.reader(infile)

    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            revenue = price * quantity

            if revenue > 100:
                writer.writerow([product, price, quantity, revenue])
                written_count += 1

print(f'Original rows: {original_count}')
print(f'Rows written: {written_count}')


print('Exersise 6:')

dirt_total = 0

with open(sales, "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
 
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])


        revenue = price * quantity
        dirt_total += revenue

        print(f'Product: {product}: ${revenue:.2f}')

print(f'Dirtreader total revenue: ${dirt_total:.2f}')    

print('Exersise 7:')

sales_summary = {}

with open(sales, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        revenue = price * quantity

        if product in sales_summary:
            sales_summary[product] += revenue
        else:
            sales_summary[product] = revenue

for product in sorted(sales_summary):
    print(f'{product}: ${sales_summary[product]:.2f}')

print('Exersise 8:')

timestamp = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f'{timestamp} | Total Revenue ${total_revenue:.2f}\n')

print('Run Log Updated Sucessfully')
