random_numbers = input("Въведи 20 случайни цели числа в диапазона [1, 30], разделени с интервал: ")
list_of_numbers = random_numbers.split(" ")
list_of_numbers_as_int = [int(num) for num in list_of_numbers]
once = []
more_than_once = []

for num in range(1, 30):
    if num in list_of_numbers_as_int:
        if list_of_numbers_as_int.count(num) == 1:
            once.append(num)
        elif list_of_numbers_as_int.count(num) > 1:
            more_than_once.append(num)

once_as_str = ", ".join(str(num) for num in once)
more_than_once_as_str = ", ".join(str(num) for num in more_than_once)

print(f"Числата, които се срещат само веднъж са: {once_as_str}")
print(f"Числата, които се повтарят повече от веднъж са: {more_than_once_as_str}")

