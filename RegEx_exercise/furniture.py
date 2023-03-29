import re
pattern = r"^>>(?P<Furniture>[A-Za-z]+)<<(?P<Integer>\d+(?P<Float>\.\d+)?)!(?P<Quantity>\d+)$"
total_cost = 0
bought_products = []
command = input()
while command != "Purchase":
    matches = re.findall(pattern, command)
    if matches:
        match = matches[0]
        furniture = match[0]
        price = match[1]
        quantity = match[3]
        bought_products.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for furn in bought_products:
    print(furn)
print(f"Total money spend: {total_cost:.2f}")
