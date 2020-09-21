def main():
    cities = ['New York','Boston','Atlanta','Dallas']

    outfile = open('22-9-63/cities.txt','w')
    outfile.writelines(cities)
    outfile.close()

main()