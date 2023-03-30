def is_even(number):
    result = number % 2 == 0
    return result


nums = [int(x) for x in input().split()]
print(list(filter(is_even,nums)))