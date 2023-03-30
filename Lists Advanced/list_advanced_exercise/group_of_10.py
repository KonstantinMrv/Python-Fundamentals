# numbers = [int(num) for num in input().split(", ")]
#
# group_of_10 = [num for num in numbers if 1 <= num <= 10]
# group_of_20 = [num for num in numbers if 11 <= num <= 20]
# group_of_30 = [num for num in numbers if 21 <= num <= 30]
# group_of_40 = [num for num in numbers if 31 <= num <= 40]
# group_of_50 = [num for num in numbers if 41 <= num <= 50]
#
# print(f"Group of 10's: {group_of_10}")
# print(f"Group of 20's: {group_of_20}")
# print(f"Group of 30's: {group_of_30}")
# print(f"Group of 40's: {group_of_40}")
# print(f"Group of 50's: {group_of_50}")

number_list = [int(n) for n in input().split(", ")]

for n in range(1, 11):
    check_list = list()
    if len(number_list) != 0:
        [check_list.append(i) for i in number_list if i <= (n * 10)]
        [number_list.remove(o) for o in check_list]
        print(f"Group of {n * 10}'s: {check_list}")