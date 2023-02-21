n = int(input())

for name in range(n):
    word = input()
    is_pure = True

    for ch in word:
        if ch == "," or ch == "." or ch == "_":
            is_pure = False
            break
    if is_pure:
        print(f'{word} is pure.')
    else:
        print(f"{word} is not pure!")
