def add(a,b):
    ans = a+b
    print(str(a) +" + "+str(b)+' = '+str(ans))


def sub(a, b):
    ans = a - b
    print(str(a)+' - '+str(b)+' = '+str(ans))


def mul(a, b):
    ans = a * b
    print(str(a)+' + '+str(b)+' = '+str(ans))


def div(a, b):
    ans = a/b
    print(str(a)+' + '+ str(b)+' = '+str(ans))


while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')

    choice = input('Enter your desired calculation keyword')

    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Enter first value'))
        b = int(input('Enter second value'))
        add(a, b)
    elif choice == 'b' or choice =='B':
        print('Subtraction')
        a = int(input('Enter your first value'))
        b = int(input('Enter your second value'))
        sub(a, b)

    elif choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('Enter your first value'))
        b = int(input('Enter your second value'))
        mul(a, b)

    elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input('Enter your first value'))
        b = int(input('Enter your sencond value'))
        div(a, b)
    else:
        quit()