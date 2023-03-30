list_of_numbers = [int(x) for x in input().split()]
num_to_remove = int(input())

list_as_string = []

for r in range(num_to_remove):
    list_of_numbers.remove(min(list_of_numbers))


print(", ".join([str(x) for x in list_of_numbers]))