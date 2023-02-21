from math import ceil

all_persons = int(input())
capacity = int(input())

all_courses = ceil(all_persons / capacity)

print(all_courses)