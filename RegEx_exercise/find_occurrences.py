import re

text = input().lower()
word = input().lower()

matches = re.findall(f"\\b{word}\\b", text)
print(len(matches))