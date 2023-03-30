operator = input()
first_number = int(input())
second_number = int(input())


def calculate(command, n1, n2):
    result = 0
    if command == "multiply":
        result = n1 * n2
    elif command == "divide":
        result = n1 // n2
    elif command == "add":
        result = n1 + n2
    elif command == "subtract":
        result = n1 - n2
    return result


res = calculate(operator, first_number, second_number)
print(res)