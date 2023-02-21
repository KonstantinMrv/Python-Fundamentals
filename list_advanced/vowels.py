vowels = ["a","o","u","e","i"]
result = [char for char in input() if char.lower() not in vowels]

print("".join(result))