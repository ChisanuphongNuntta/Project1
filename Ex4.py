print("Please select operation : ")
print("1.Add \n2.Subtract \n3.Multply \n4.Divide")
operation = int(input("Select opration from: 1, 2, 3, 4, :1 = "))
first = int(input("Enter your first number : "))
second = int(input("Enter your second number  : "))
if operation == 1 :
    print(">> ",first," + ", second," = ",(first+second))
elif operation == 2 :
    print(">> ",first," - ",second," = ",(first-second) )
elif operation == 3 :
    print(">> ",first," x ",second," = ",(first*second))
elif operation == 4 :
    print(">> ",first," ÷ ",second," = ",(first/second))
else:
    print("!!Error!! Don't have opration")