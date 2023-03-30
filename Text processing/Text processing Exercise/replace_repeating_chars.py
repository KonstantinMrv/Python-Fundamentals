string = input()

result = string[0]

for ch in string:
    if ch == result[-1]:
        continue
    else:
        result += ch

print(result)