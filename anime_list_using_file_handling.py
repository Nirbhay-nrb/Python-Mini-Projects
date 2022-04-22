from ctypes import sizeof


file = 'anime_list.txt'

def newAnime():
    anime = input('Enter anime name: ')
    with open(file,'a') as f:
        f.write(f'{anime}\n')
    print('Added successfully\n')
    print('----------------\n\n')

def display():
    with open(file,'r') as f:
        for line in f:
            print(line,end='')
    print('----------------\n\n')

def count():
    with open(file,'r') as f:
        anime = f.readlines()
        print('Number of animes watched:',len(anime))
    print('----------------\n\n')

while True:
    option = input('1. New anime\n2. Display list\n3. Number of animes watched\n4. Exit\nYour choice: ')
    if option=='1':
        print('\n\n----------------')
        newAnime()
    elif option=='2':
        print('\n\n----------------')
        display()
    elif option=='3':
        print('\n\n----------------')
        count()
    else:
        print('\n\n----------------')
        print('Thanks!!\nExiting')
        break
