n = int(input())
even = []
odd = []
positive = []
negative = []

for _ in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)
    if current_number < 0:
        negative.append(current_number)
    else:
        positive.append(current_number)

command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
else:
    print(negative)