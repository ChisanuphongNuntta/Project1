filename = input('Enter the filename : ')
if filename.endswith('.txt'):
    print('That is the name of a text file.')
elif filename.endswith('.py'):
    print('That is the name of a pyhton soure file.')
elif filename.endswith('.doc'):
    print('That is the name of a word processing docuent.')
else:
    print('Unknow file type')