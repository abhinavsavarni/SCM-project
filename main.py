import random



print("welcome to your password generator")

char1 = 'abcdefghijklmnopqrstuvwxyz'
char2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char3 = '!@#$%^&*()/?.,1234567890'


a = 8
num=1

for i in range(num):
     passwords = ''
for x in range(a):
    passwords += random.choice(char1 + char2 + char3)


print(passwords)
