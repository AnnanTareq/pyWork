import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    password_length = int(input('How long your password should be? '))

    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


option = input('Do you want to generate password? press (Y/N) ')

if option == 'Y' or option == 'y':
    generate_password()
elif option == 'N' or option == 'n':
    print('Program ended')
    quit()
else:
    print('Invalid Input')
    quit()