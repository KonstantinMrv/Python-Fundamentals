quantity_by_product = {}
price_by_product = {}

command = input()
while command != "buy":
    command_args = command.split()
    product = command_args[0]
    price = float(command_args[1])
    quantity = int(command_args[2])

    price_by_product[product] = price
    if product in quantity_by_product:
        quantity_by_product[product] += quantity
    else:
        quantity_by_product[product] = quantity

    command = input()

for product in price_by_product:
    price = price_by_product[product]
    quantity = quantity_by_product[product]
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")