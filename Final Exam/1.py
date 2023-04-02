string = input()

line = input()
while line != "End":
    command_args = line.split()
    command = command_args[0]

    if command == "Translate":
        char = command_args[1]
        replacement = command_args[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == "Includes":
        substring = command_args[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif command == "Start":
        substring = command_args[1]
        is_starting = string.startswith(substring)
        print(is_starting)
    elif command == "Lowercase":
        string = string.lower()
        print(string)
    elif command == "FindIndex":
        char = command_args[1]
        index = string.rindex(char)
        print(index)
    elif command == "Remove":
        start_index = int(command_args[1])
        count = int(command_args[2])
        string = string[:start_index] + string[start_index + count:]
        print(string)
    line = input()