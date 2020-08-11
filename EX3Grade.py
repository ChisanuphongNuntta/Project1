import time
grade = float(input("Enter your score : "))
if grade >= 90:
    print("Grade A")
elif grade >= 80:
    print("Grade B")
elif grade >= 70:
    print("Grade C")
elif grade >= 60:
    print("Grade D")
elif grade < 60:
    print("Grade F")
h =time.time()
print((time.time()-h)*1000) 