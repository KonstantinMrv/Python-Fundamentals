n = int(input())
name_by_license_plate = {}

for _ in range(n):
    line = input().split()
    command = line[0]
    name = line[1]

    if command == "register":
        license_plate = line[2]
        if name in name_by_license_plate:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            name_by_license_plate[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
    else:
        if name in name_by_license_plate:
            name_by_license_plate.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, plate in name_by_license_plate.items():
    print(f"{name} => {plate}")