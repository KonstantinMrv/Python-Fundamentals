number_of_electrons = int(input())
new_list = []
position_of_shell = 0

while 0 < number_of_electrons:

    position_of_shell += 1
    shell = 2 * position_of_shell ** 2

    if number_of_electrons >= shell:
        new_list.append(shell)
        number_of_electrons -= shell
    else:
        new_list.append(number_of_electrons)
        number_of_electrons = 0

print(new_list)