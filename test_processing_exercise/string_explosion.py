string = input().split(">")
previous = 0

result = [string[0]]
for part in string[1:]:
    power = int(part[0])
    previous += power

    new = part[previous:]
    previous = max(previous - len(part), 0)
    result.append(new)

print(">".join(result))
