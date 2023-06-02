animals = input().split(", ")
wolf = animals.index("wolf")
sheep_count = len(animals) - 1

if wolf == sheep_count:
    print("Please go away and stop eating my sheep")
else:
    sheep_number = sheep_count - wolf
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")