lines = int(input())

result = 0
for _ in range(lines):
    symbol = input()
    result += ord(symbol)

print(f"The sum equals: {result}")