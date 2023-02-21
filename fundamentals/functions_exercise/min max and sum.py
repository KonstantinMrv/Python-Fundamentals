# def is_max(numbers):
#     return max(nums)
#
#
# def is_min(numbers):
#     return min(nums)
#
#
# def total_sum(numbers):
#     total_sum = 0
#     for n in nums:
#         total_sum += n
#     return total_sum
#
#
# nums = [int(x) for x in input().split()]
#
# min_num = is_min(nums)
# max_num = is_max(nums)
# sum = total_sum(nums)
#
# print(f"The minimum number is {min_num}")
# print(f"The maximum number is {max_num}")
# print(f"The sum number is: {sum}")

nums = [int(x) for x in input().split()]

print(f"The minimum number is {min(nums)}")
print(f"The maximum number is {max(nums)}")
print(f"The sum number is: {sum(nums)}")
