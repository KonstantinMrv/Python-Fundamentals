def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


first_number = int(input())
second_number = int(input())
third_number = int(input())

result_from_add = add(first_number, second_number)
total_sum = subtract(result_from_add, third_number)

print(total_sum)