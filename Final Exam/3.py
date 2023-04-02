
likes_by_username = {}
comments_by_username = {}

line = input()
while line != "Log out":
    line_args = line.split(":")
    command = line_args[0]
    u = line_args[1]
    username = u.strip()
    if command == "New follower":

        if username in likes_by_username:
            line = input()
            continue
        likes_by_username[username] = 0
        comments_by_username[username] = 0
    elif command == "Like":
        likes = int(line_args[2])
        if username not in likes_by_username:
            likes_by_username[username] = likes
            comments_by_username[username] = 0
        else:
            likes_by_username[username] += likes
    elif command == "Comment":
        if username not in likes_by_username:
            likes_by_username[username] = 0
            comments_by_username[username] = 1
        else:
            comments_by_username[username] += 1
    else:
        if username in likes_by_username:
            del likes_by_username[username]
            del comments_by_username[username]
        else:
            print(f"{username} doesn't exist.")

    line = input()

print(f"{len(likes_by_username)} followers")
for username, likes in likes_by_username.items():
    print(f"{username}: {likes + comments_by_username[username]}")

