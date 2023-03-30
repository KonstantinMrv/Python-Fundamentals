from string import digits, ascii_letters

usernames = input().split(", ")
valid_ch = ascii_letters + digits + "-" + "_"

for username in usernames:
    valid_length = False
    valid_symbols = True

    if 3 <= len(username) <= 16:
        valid_length = True
    else:
        continue

    for ch in username:
        if ch not in valid_ch:
            valid_symbols = False
            break

    if valid_symbols and valid_length:
        print(username)



