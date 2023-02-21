while True:
    line = input()

    if line == "End":
        break
    if line == "SoftUni":
        continue

    for ch in line:
        print(f'{ch}{ch}', end='')
    print()