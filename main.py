print("welcome to your password generator")

char1 = 'abcdefghijklmnopqrstuvwxyz'
char2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char3 = '!@#$%^&*()/?.,1234567890'

num = int(input('amount of passwords to generate: '))
a = int(input('your password length: '))

print(
    "Which type of password do you want??\n1.Only small aphabets\n2.Capitalized alphabets\n3.Only special characters plus Numericals\n4.Password with all characters\n")
choice = int(input())

while (True):
    if (choice < 1 or choice > 4):
        print("Enter a valid choice:")
        choice = int(input())
        continue
    print('here are your passwords: ')
    if (choice == 1):
        for i in range(num):
            passwords = ''
            for x in range(a):
                passwords += random.choice(char1)
            print(passwords)
    elif (choice == 2):
        for i in range(num):
            passwords = ''
            for x in range(a):
                passwords += random.choice(char2)
            print(passwords)
    elif (choice == 3):
        for i in range(num):
            passwords = ''
            for x in range(a):
                passwords += random.choice(char3)
            print(passwords)

    elif (choice == 4):
        for i in range(num):
            passwords = ''
            for x in range(a):
                passwords += random.choice(char1 + char2 + char3)
            print(passwords)
    break
    break