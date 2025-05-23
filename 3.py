import csv
total_cost = 0

with open('products.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    print("Нужно купить:")
    for product, quantity, price in reader:
        total_price = int(price) * int(quantity)
        total_cost += total_price
        print(f"{product} - {quantity} шт. за {price} руб.")
print(f"\nИтоговая сумма: {total_cost} руб.")
