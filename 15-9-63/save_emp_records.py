def main():
    num_epm = int(input('How many employee records ' +\
                        'do you want to create? '))
    emp_file = open('15-9-63/employees.txt','w')
    for count in range(1,num_epm + 1):
        print('Enter data for employee #',count,sep='')
        name = input('Name : ')
        id_num = input('ID number : ')
        dept = input('Department : ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

    emp_file.close()
    print('Employ records written to employees.txt.')

main()