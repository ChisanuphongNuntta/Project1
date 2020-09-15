def main():
    filename = input('Enter a filename : ')
    try:
        infile = open('15-9-63/'+filename,'r')
        contents = infile.read()
        print(contents)
        infile.close()
    except IOError:
        print('An error occurred try to read')
        print('the file','15-9-63/'+filename)
main()
