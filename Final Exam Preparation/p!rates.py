city_population = {}
city_gold = {}

command = input()
while command != "Sail":
    command_args = command.split("||")
    city = command_args[0]
    population = int(command_args[1])
    gold = int(command_args[2])

    if city not in city_population:
        city_population[city] = population
    else:
        city_population[city] += population
    if city not in city_gold:
        city_gold[city] = gold
    else:
        city_gold[city] += gold

    command = input()

action = input()
while action != "End":
    action_args = action.split("=>")
    order = action_args[0]

    if order == "Plunder":
        targeted_city = action_args[1]
        people = int(action_args[2])
        gold_stolen = int(action_args[3])

        city_population[targeted_city] -= people
        city_gold[targeted_city] -= gold_stolen
        print(f"{targeted_city} plundered! {gold_stolen} gold stolen, {people} citizens killed.")
        if city_population[targeted_city] <= 0 or city_gold[targeted_city] <= 0:
            del city_population[targeted_city]
            del city_gold[targeted_city]
            print(f"{targeted_city} has been wiped off the map!")

    elif order == "Prosper":
        targeted_city = action_args[1]
        growth = int(action_args[2])

        if growth < 0:
            print(f"Gold added cannot be a negative number!" )
        else:
            city_gold[targeted_city] += growth
            print(f"{growth} gold added to the city treasury. {targeted_city} now has {city_gold[targeted_city]} gold.")
    action = input()

if city_population:
    print(f"Ahoy, Captain! There are {len(city_population)} wealthy settlements to go to:")
    for city, population in city_population.items():
        print(f"{city} -> Population: {population} citizens, Gold: {city_gold[city]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")