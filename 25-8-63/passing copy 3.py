def reverse_name(first,last):
    print(first,last)
    s1 = (first[::-1])
    s2 = (last[::-1])
    print(s2,s1)

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name,last_name)

main()