string = input()

for idx in range(len(string)):
    ch = string[idx]
    if ch == ":":
        symbol = string[idx + 1]
        print(f":{symbol}")