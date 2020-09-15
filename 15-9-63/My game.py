read_friend = 1
add_friend = 2
del_friend = 3
end = 4

def main():
    try:
        choice = 0 
        while choice != end:
            display_manu()
            choice = int(input('Enter your choice : '))
            if choice == read_friend:
                text = open('15-9-63/game.txt','r')
                t = text.read()
                print(t)
                text.close()
            elif choice == add_friend:
                inn = input('Add your friend : ')
                text2 = open('15-9-63/game.txt','a')
                text2.write(inn+'\n')
                text2.close()
            elif choice == del_friend:
                deltext = input('Enter your delete : ')
                detext = open('15-9-63/game.txt','a')
                detext.clear(deltext)
                detext.close()
            elif choice == end:
                print('end program...')
            else:
                print('Error')
    except Exception as err:
        print(err)

def display_manu():
    print('    menu')
    print('1. read friend')
    print('2. add friend')
    print('3. delete your friend')
    print('4. end program')

main()
