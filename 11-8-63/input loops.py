#get a test score.
score = int(input('Enter a test score : '))
#Make sure it is not less than 0 or greater than 100.
while score < 0 or score > 100 :
    print('Error : The schore cannot be negative')
    print('or greater than 100.')
    score = int(input('Enter tne correct score : '))