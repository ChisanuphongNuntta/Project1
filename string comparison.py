hours = float(input("Enter the number of hours worked : "))
rate = float(input("enter the hourly pay rate : "))
sum_over = (hours - 40) * 1.5
sum_hours = (40 * rate)
if hours > 40:
    print("The gross pay is : ",sum_hours + (sum_over * rate))
else:
    print("The gross pay is : ",hours*rate)