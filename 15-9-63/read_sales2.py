def main():
    sales_file = open('15-9-63/sales.txt','r')

    for line in sales_file:
        amount = float(line)
        print(format(amount,'.2f'))

    sales_file.close()

main()