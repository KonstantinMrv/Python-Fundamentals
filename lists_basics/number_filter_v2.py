n = int(input())

all_numbers = []

for _ in range(n):
    current_number = int(input())
    all_numbers.append(current_number)

command = input()

for el in all_numbers:
    if command == "even":
        if el % 2 != 0:
            all_numbers.remove(el)
    elif command == "odd":
        if el % 2 != 1:
            all_numbers.remove(el)
    elif command == "positive":
        if el < 0:
            all_numbers.remove(el)
    elif command == "negative":
        if el >= 0:
            all_numbers.remove(el)

print(all_numbers)