strings = input().split()

first = strings[0]
second = strings[1]

min_len = min(len(first), len(second))
total_sum = 0

for idx in range(min_len):
    str1 = first[idx]
    str2 = second[idx]
    total_sum += ord(str1) * ord(str2)

for idx in range(min_len, len(first)):
    total_sum += ord(first[idx])

for idx in range(min_len, len(second)):
    total_sum += ord(second[idx])
print(total_sum)