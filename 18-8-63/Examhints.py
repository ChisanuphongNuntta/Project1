inputmsg = input("In put string you want to swap word : ")
print(inputmsg.split())
separatewords = inputmsg.split()

print("separate word")
for i in separatewords:
    print(i)

print("Modifly each word")
print(len(separatewords))
for j in range(len(separatewords)):
    separatewords[j] = 'G' + separatewords[j]
    print(separatewords[j])

print(separatewords)
print(" ".join(separatewords),)