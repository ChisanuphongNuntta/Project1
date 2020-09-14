def main():
    emp_open = open('employees.txt','r')
    line = emp_open.read()
    print('Name : ',line)       

    emp_open.close()
    
main()