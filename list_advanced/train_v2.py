wagons = int(input())
train = [0] * wagons
length = len(train)

command = input()
while command != "End":
    split_data = command.split()
    action = split_data[0]
    if action == "add":
        people = int(split_data[1])
        train[-1] += people
    elif action == "insert":
        people = int(split_data[2])
        wagon_idx = int(split_data[1])
        train[wagon_idx] += people
    elif action == "leave":
        people = int(split_data[2])
        wagon_idx = int(split_data[1])
        train[wagon_idx] -= people

    command = input()

print(train)