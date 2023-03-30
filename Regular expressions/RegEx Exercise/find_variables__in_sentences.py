import re

text = input()

matches = re.findall(r"\b_([A-Za-z0-9]+)\b", text)

print(*matches, sep=",")
# print(",".join(matches)) -Едно и също принтиране