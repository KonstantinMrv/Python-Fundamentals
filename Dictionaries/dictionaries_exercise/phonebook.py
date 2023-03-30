phonebook = {}

n = 0
while True:
    line = input().split("-")
    if len(line) == 1:
        n += int(line[0])
        break

    name = line[0]
    number = line[1]
    phonebook[name] = number

for _ in range(n):
    person = input()
    if person in phonebook:
        print(f"{person} -> {phonebook[person]}")
    else:
        print(f"Contact {person} does not exist.")