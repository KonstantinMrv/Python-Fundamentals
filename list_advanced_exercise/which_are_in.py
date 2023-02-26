first_list = input().split(", ")
second_list = input().split(", ")

new_list = []

for sequence1 in first_list:
    for sequence2 in second_list:
        if sequence1 in sequence2:
            new_list.append(sequence1)
            break
        else:
            continue

print(new_list)
