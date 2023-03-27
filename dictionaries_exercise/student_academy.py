student_by_grades = {}

n = int(input())

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in student_by_grades:
        student_by_grades[student] = []
    student_by_grades[student].append(grade)

for student, grades in student_by_grades.items():
    average = sum(grades) / len(grades)
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")
