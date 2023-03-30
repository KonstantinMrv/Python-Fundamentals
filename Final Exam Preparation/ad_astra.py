import re

pattern = r"#[A-Za-z ]+#\d{2}\/\d{2}\/\d{2}#\d+#|\|[A-Za-z ]+\|\d{2}\/\d{2}\/\d{2}\|\d+\|"

text = input()
kcal_per_day = 2000
total_kcal = 0
valid_food = []
matches = re.findall(pattern, text)
for match in matches:
    if match[0] == "#":
        match_args = match.split("#")
        food = match_args[1]
        best_before = match_args[2]
        kcal = int(match_args[3])
        total_kcal += kcal
    else:
        match_args = match.split("|")
        food = match_args[1]
        best_before = match_args[2]
        kcal = int(match_args[3])
        total_kcal += kcal

left_days = total_kcal // kcal_per_day
print(f"You have food to last you for: {left_days} days!")
for match in matches:
    if match[0] == "#":
        match_args = match.split("#")
        food = match_args[1]
        best_before = match_args[2]
        kcal = int(match_args[3])
        print(f"Item: {food}, Best before: {best_before}, Nutrition: {kcal}")
    else:
        match_args = match.split("|")
        food = match_args[1]
        best_before = match_args[2]
        kcal = int(match_args[3])
        print(f"Item: {food}, Best before: {best_before}, Nutrition: {kcal}")