resources = {}

command = input()
while command != "stop":
    quantity = int(input())

    if command in resources:
        resources[command] += quantity
    else:
        resources[command] = quantity
    command = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")