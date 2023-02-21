factor = int(input())
count = int(input())

lst = []

for num in range(1, count + 1):
    # current_number = num * factor
    lst.append(num * factor)

print(lst)