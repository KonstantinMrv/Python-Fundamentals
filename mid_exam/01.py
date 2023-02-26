needed_xp_to_unlock = float(input())
battles_count = int(input())
total_xp_gained = 0
battle_counter = 0

for _ in range(battles_count):
    player_xp = float(input())
    battle_counter += 1
    total_xp_gained += player_xp
    if battle_counter % 3 == 0:
        total_xp_gained += player_xp * 0.15
    if battle_counter % 5 == 0:
        total_xp_gained -= player_xp * 0.10
    if battle_counter % 15 == 0:
        total_xp_gained += player_xp * 0.5
    if total_xp_gained >= needed_xp_to_unlock:
        print(f"Player successfully collected his needed experience for {battle_counter} battles.")
        exit(0)

if total_xp_gained < needed_xp_to_unlock:
    xp_left = needed_xp_to_unlock - total_xp_gained
    print(f"Player was not able to collect the needed experience, {xp_left:.2f} more needed.")
