rooms = int(input())

free_chairs = 0
is_game_on = True

for room in range(1, rooms + 1):
    chairs, visitors = input().split()
    if len(chairs) > int(visitors):
        free_chairs += len(chairs) - int(visitors)
    elif len(chairs) < int(visitors):
        needed_chairs = int(visitors) - len(chairs)
        is_game_on = False
        print(f"{needed_chairs} more chairs needed in room {room}")

if is_game_on:
    print(f"Game On, {free_chairs} free chairs left")
