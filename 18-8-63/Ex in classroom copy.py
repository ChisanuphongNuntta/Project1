str1 = "English = 78 Science = 83 Math = 68 History = 65"
num = (str1.split())
sum = 0
z = 0
for x in num:
    if x.isnumeric() :
        sum = sum + int(x)
        z = z + 1
print("sum is : ",sum)
print("average is : ",sum/z)
        
        