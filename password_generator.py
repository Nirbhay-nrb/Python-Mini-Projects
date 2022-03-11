from cgitb import small
import random
import string
n = int(input('Enter the length of password: '))
small_alphas = list(string.ascii_lowercase)
capital_alphas = list(string.ascii_uppercase)
special_characters = list(string.punctuation)
password = ''
for i in range(n):
    kind = random.randint(1,3)
    if kind==1:
        password += random.choice(small_alphas)
    elif kind==2:
        password += random.choice(capital_alphas)
    else:
        password += random.choice(special_characters)
print('Your password =',password)