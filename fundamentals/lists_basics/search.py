n = int(input())
word = input()

all_commands = []
filtered_list = []

for _ in range(n):
    current_command = input()
    all_commands.append(current_command)
    if word in current_command:
        filtered_list.append(current_command)

print(all_commands)
print(filtered_list)