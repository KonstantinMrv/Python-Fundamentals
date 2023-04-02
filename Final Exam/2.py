import re

n = int(input())
pattern = r"\|[A-Z]{4,}\|:#[A-Za-z]+ [A-Za-z]+#"

for _ in range(n):
    name_and_title = input()
    match = re.findall(pattern, name_and_title)
    if match:
        input_split = name_and_title.split(":")
        name = input_split[0]
        title = input_split[1]
        clear_name = name.replace("|", "")
        clear_title = title.replace("#", "")
        print(f"{clear_name}, The {clear_title}")
        print(f">> Strength: {len(clear_name)}")
        print(f">> Armor: {len(clear_title)}")
    else:
        print("Access denied!")
