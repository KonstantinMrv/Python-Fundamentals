def get_largest_number(number):
    digit = list(str(number))

    digit.sort(reverse=True)
    largest_num = "".join(digit)
    return largest_num

numbers = int(input())
largest = get_largest_number(numbers)

print(largest)