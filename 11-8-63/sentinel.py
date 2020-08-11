keep_going = 'y'
cost = 2.5
while keep_going == 'y' or keep_going == "Y":
    sales = float(input("Enter the item's wholesale cost : "))
    commission = sales * cost
    print('Retail price : ', \
    format(commission,',.2f'), sep='')
    keep_going = input('Do you have another item ?' + \
                           '(Enter y for yes) : ')