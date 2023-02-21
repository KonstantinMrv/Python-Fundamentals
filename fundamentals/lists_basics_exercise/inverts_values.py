# nums = input().split()
# lst = []
#
# for el in nums:
#     int_el = int(el)
#     reversed_el = int(el) * -1
#     lst.append(reversed_el)
#
# print(lst)

nums = [int(x) * -1 for x in input().split()]
print(nums)

