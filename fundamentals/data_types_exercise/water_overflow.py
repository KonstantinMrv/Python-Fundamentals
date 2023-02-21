capacity = 255

lines = int(input())
tank = 0

for _ in range(lines):
    liters = int(input())
    if tank + liters > capacity:
        print("Insufficient capacity!")
    else:
        tank += liters

print(tank)



