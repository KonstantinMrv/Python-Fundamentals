numbers = [int(x) for x in input().split()]

command = input()
while command != "Finish":
    command_args = command.split()
    command = command_args[0]
    value = int(command_args[1])
    if command == "Add":
        numbers.append(value)
    elif command == "Remove":
        if value in numbers:
            numbers.remove(value)
        else:
            command = input()
            continue
    elif command == "Replace":
        if value in numbers:
            replacement = int(command_args[2])
            value_index = numbers.index(value)
            numbers.remove(value)
            numbers.insert(value_index, replacement)
        else:
            command = input()
            continue

    elif command == "Collapse":
        for num in numbers:
            if num < value:
                numbers.remove(num)
                numbers.insert(0, 0)


    command = input()


result = [el for el in numbers if el != 0]
print(*result, sep = ' ')