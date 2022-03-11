import random
choices = ['Rock','Paper','Scissors']
while True:
    run = int(input('Press any number to play or press 0 to exit: '))
    if run==0: 
        break
    userChoice = int(input('\n\nEnter the number corresponding to your choice:\n1. Rock\n2. Paper\n3. Scissors\n'))
    if userChoice not in [1,2,3]:
        print('Incorrect choice')
        continue
    cpuChoice = random.randint(1,3)
    res = 0
    if cpuChoice==userChoice:
        res = 1 # tie
    elif (cpuChoice==1 and userChoice==2) or (cpuChoice==2 and userChoice==3) or (cpuChoice==3 and userChoice==1):
        res = 2 # User won
    else :
        res = 3 # User lost
    print('\n\nYour choice =',choices[userChoice-1])
    print('CPU\'s choice =',choices[cpuChoice-1])
    print('---RESULT---')
    if res==1:
        print('Tie')
    elif res==2:
        print('Yayyy!! You won!!')
    else:
        print('You lose, better luck next time!!')
print('Thanks for playing!!')