import re

pattern = r"(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"
links = []
text = input()
while True:
    if not text:
        break
    matches = re.findall(pattern, text)
    links.extend([m[0] for m in matches])
    text = input()

for link in links:
    print(link)
