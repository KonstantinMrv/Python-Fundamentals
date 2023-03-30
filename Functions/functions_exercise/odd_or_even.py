def all_sum(num):
    even_sum = 0
    odd_sum = 0

    for num in number_as_string:
        number = int(num)
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    return [even_sum, odd_sum]


number_as_string = input()


result = all_sum((number_as_string))
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")
