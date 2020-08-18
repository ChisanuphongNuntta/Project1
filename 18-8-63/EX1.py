fname = str(input("Enter your frist name : "))
lname = str(input("Enter your last name : "))
numberID = (input("Enter your student ID number : "))
print("Your system login name is : "+fname[:3]+lname[:3]+numberID[-3:])