initial_version = [int(x) for x in input().split(".")]

initial_version[2] += 1
if initial_version[2] == 10:
    initial_version[2] = 0
    initial_version[1] += 1
    if initial_version[1] == 10:
        initial_version[1] = 0
        initial_version[0] += 1

print(*initial_version, sep = '.')
