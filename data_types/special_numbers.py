n = int(input())

for num in range(1, n + 1):
    is_special = False
    sum_num = 0
    num_as_string = str(num)

    for char in num_as_string:
        sum_num += int(char)
    if sum_num == 5 or sum_num == 7 or sum_num == 11:
        is_special = True
    print(f"{num} -> {is_special}")