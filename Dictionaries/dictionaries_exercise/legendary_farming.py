key_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item_by_material = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk = {}

crafted = False
while not crafted:
    line = input()
    materials = line.split()

    for idx in range(0, len(materials) - 1, 2):
        quantity = int(materials[idx])
        material = materials[idx + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                crafted = True
                print(f"{legendary_item_by_material[material]} obtained!")
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity

for material, count in key_materials.items():
    print(f"{material}: {count}")
for material, count in junk.items():
    print(f"{material}: {count}")