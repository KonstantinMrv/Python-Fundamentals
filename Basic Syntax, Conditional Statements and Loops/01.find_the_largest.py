numbers = input()
result = []

for el in numbers:
    num = int(el)
    result.append(num)

sorted_result = list(sorted(result))
reverse_result = list(reversed(sorted_result))
print("".join([str(x) for x in reverse_result]))
