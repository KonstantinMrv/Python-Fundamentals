orders = int(input())

total_price = 0
for _ in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if capsule_price < 0.01 or capsule_price > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    order_price = (capsule_price * capsules_per_day) * days
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_price:.2f}")