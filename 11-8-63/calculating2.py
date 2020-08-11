#program to find the sum of all numbers stored in a list
#List of numbers
numbers = [6,5,3,8,4,2,5,4,11]

#varible to store the sum
sum = 0 

#iterate over the list
for val in numbers:
    sum += val
    print(sum)

print("the sum is", sum)