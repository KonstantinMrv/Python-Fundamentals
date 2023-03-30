names = input().split(", ")

sorted_names = (sorted(names, key=lambda x: -(len(x)m, x))
print(sorted_names)