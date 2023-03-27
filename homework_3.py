random_numbers = input("Въведи 20 случайни цели числа в диапазона [1, 30], разделени с интервал: ")
list_of_numbers = random_numbers.split(" ")
list_of_numbers_as_int = [int(num) for num in list_of_numbers]
once = []

for num in range(1, 30):
    if num in list_of_numbers_as_int:
        if list_of_numbers_as_int.count(num) == 1:
            once.append(num)
        elif list_of_numbers_as_int.count(num) > 1:
            print(f"Числото {num} се повтаря {list_of_numbers_as_int.count(num)} пъти!")

once_as_str = ", ".join(str(num) for num in once)
print(f"Числата, които се срещат само веднъж са: {once_as_str}")


