cards = input().split()

should_terminate = False
first_team_sent_off_counter = 0
second_team_sent_off_counter = 0
A_team_sent_off_player = []
B_team_sent_off_player = []

for card in cards:
    if card in A_team_sent_off_player or card in B_team_sent_off_player:
        continue
    card_args = card.split("-")
    team_name = card_args[0]
    player = card_args[1]

    is_first_team = team_name == "A"
    if is_first_team:
        A_team_sent_off_player.append(card)
        first_team_sent_off_counter += 1
    else:
        B_team_sent_off_player.append(card)
        second_team_sent_off_counter += 1

    if first_team_sent_off_counter > 4 or second_team_sent_off_counter > 4:
        should_terminate = True

first_team_remaining_player = 11 - first_team_sent_off_counter
second_team_remaining_player = 11 - second_team_sent_off_counter


print(f"Team A - {first_team_remaining_player}; Team B - {second_team_remaining_player}")


if should_terminate:
    print("Game was terminated")