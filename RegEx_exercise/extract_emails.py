import re

text = input()

matches = re.findall(r" [A-Za-z0-9][\w\-.]+[A-Za-z0-9]@[a-z][a-z\-]+\.[a-z.]+\b", text)

print(*matches, sep="\n")