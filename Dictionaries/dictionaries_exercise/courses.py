student_by_course = {}

command = input()
while command != "end":
    command_args = command.split(" : ")
    course = command_args[0]
    student = command_args[1]

    if course not in student_by_course:
        student_by_course[course] = []

    if student not in student_by_course:
        student_by_course[course].append(student)

    command = input()

for course, students in student_by_course.items():
    print(f"{course}: {len(students)}")

    for student in student_by_course[course]:
        print(f"-- {student}")