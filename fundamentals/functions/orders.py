def calculate(product, quantity):
    result = 0
    if product == "water":
        result = quantity * 1
    elif product == "coffee":
        result = quantity * 1.5
    elif product == "coke":
        result = quantity * 1.4
    elif product == "snacks":
        result = quantity * 2
    return result


order = input()
n = int(input())

res = calculate(order, n)
print(f"{res:.2f}")
