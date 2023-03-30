string = input()
new_string = ""

for ch in string:
    new_ch = ord(ch) + 3
    new_string += chr(new_ch)

print(new_string)