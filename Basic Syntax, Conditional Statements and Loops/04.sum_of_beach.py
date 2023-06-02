text = input().lower()

sand_count = text.count("sand")
fish_count = text.count("fish")
water_count = text.count("water")
sun_count = text.count("sun")

print(sun_count + fish_count + water_count + sand_count)