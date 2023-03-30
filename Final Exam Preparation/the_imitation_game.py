message = input()

command = input()
while command != "Decode":
    command_args = command.split("|")
    action = command_args[0]
    if action == "Move":
        n = int(command_args[1])
        message = message[n:] + message[:n]

    elif action == "Insert":
        index = int(command_args[1])
        value = command_args[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]
        message = message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {message}")