employees_by_company = {}

command = input()
while command != "End":
    command_args = command.split(" -> ")
    company = command_args[0]
    employee = command_args[1]

    if company not in employees_by_company:
        employees_by_company[company] = []

    if employee not in employees_by_company[company]:
        employees_by_company[company].append(employee)

    command = input()

for company, employee in employees_by_company.items():
    print(company)
    for id in employee:
        print(f"-- {id}")