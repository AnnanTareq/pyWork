import random

questionBank = {}
ans = set()
marks = 0


def addQuestion(question, answer):
    questionBank.__setitem__(question, answer)


def qz(marks=0):
    for key in questionBank.keys():
        print('Your questions is : \n', key)
        lst = questionBank.get(key)
        list(lst)
        random.shuffle(lst)
        for i in range(len(lst)):
            print(i + 1, '.', lst[i])

        c = input('Enter your answer here : ')

        if c in ans:
            marks += 1
            print('Your Answer Is Correct')
        else:
            print('Your answer is wrong')
        print('Achieved marks = ', marks)


while input('Do you want to add question? press: y, otherwise press any key == ') == 'y':
    a = input('Enter question : ')
    b = input('Enter original answer : ')
    ans.add(b)
    c = list()
    c.append(b)

    size = 0
    while True:
        try:
            size = int(input('Enter desired option length : '))
        except ValueError:
            print("You doesn't enter integer value")
            continue
        else:
            print('Now integer found')
            break

    for i in range(size):
        option = input(f'{i+1} Enter others option : ')
        while option == '' or option == ' ':
            option = input(f'{i+1} please Enter other option again : ')

        while option not in c:
            c.append(option)
            print('Input successful')
            break
        else:
            print('Your entered value does exist in list, Please Enter again')
            newOpt = input('Enter your option element again: ')
            while newOpt == '' or newOpt == ' ':
                print('Empty strings are not acceptable')
                newOpt = input('Please enter again : ')

            while newOpt in c:
                newOpt = input('Please Enter Again : ')
            else:
                c.append(newOpt)
                print('Input Successful!!!')
                i += 1

    addQuestion(a, c)

print('\n', '*' * 40)
qz()
