numbers = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(numbers)):
    beggar_idx = idx % beggars_count
    input_numbers = int(numbers[idx])
    beggars[beggar_idx] += input_numbers

print(beggars)