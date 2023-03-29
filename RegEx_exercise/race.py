import re
name_pattern = r"[A-Za-z]"
digit_pattern = r"[\d]"
names_with_dist = {}
participants = input().split(", ")
for participant in participants:
    names_with_dist[participant] = 0


command = input()
while command != "end of race":
    distance_match = re.findall(digit_pattern, command)
    distance = sum([int(num) for num in distance_match])
    name_match = re.findall(name_pattern, command)
    name = "".join(letter for letter in name_match)

    if name in names_with_dist.keys():
        names_with_dist[name] += distance

    command = input()

name_of_participants = sorted(names_with_dist.items(), key=lambda x: -x[1])

print(f"1st place: {name_of_participants[0][0]}")
print(f"2nd place: {name_of_participants[1][0]}")
print(f"3rd place: {name_of_participants[2][0]}")