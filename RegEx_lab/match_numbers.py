import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

numbers = input()

matches = re.finditer(pattern, numbers)
for match in matches:
    print(match.group(), end=" ")
