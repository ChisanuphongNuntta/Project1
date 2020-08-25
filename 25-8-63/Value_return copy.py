def get_name():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    return first, last

first_name,last_name = get_name()
print('First name : ',first_name,' Last name : ',last_name)

if len(last_name) %2 == 0:
    print('Password : ',first_name[:3]+(last_name)[(len(last_name)//2)-2:(len(last_name)//2)+1])
else:
    print('Password : ',first_name[:3]+(last_name)[(len(last_name)//2)-1:(len(last_name)//2)+2])
