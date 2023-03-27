countries = input().split(", ")
capitals = input().split(", ")

capitals_by_countries = {}

# for country, capital in zip(country_name, capital_name):
#     print(f"{country} -> {capital}")

for idx in range(len(countries)):
    country = countries[idx]
    capital = capitals[idx]
    capitals_by_countries[country] = capital

for country, capital in capitals_by_countries.items():
    print(f"{country} -> {capital}")

