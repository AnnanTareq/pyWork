import random

matrix = [['D', 'W', 'L'],
          ['L', 'D', 'W'],
          ['W', 'L', 'D']
          ]
compInputLst = [0, 1, 2]
usrpoints = 0
cmppoints = 0


def inputfunc():
    ci = random.choice(compInputLst)
    try:
        '''
            Try to prevent input more than or equal to 3
        '''
        userInput = int(input('Enter your value: '))
        while userInput > 2:                                    # this check will be preventing to take user input more than 3
            i = 0
            while i < 1:
                try:                                            # this block will prevent value error
                    userInput = int(input('Enter again : '))
                    break
                except ValueError:
                    i = 0
            if userInput < 3:
                break
        print(matrix[userInput][ci])
        checkAns(userInput, ci)

    except ValueError:
        i = 0
        while i < 1:
            check = input('Do you want to add any input anymore? press : y = ')
            if check.lower() == 'y':
                try:
                    userInput = int(input('enter'))
                    while userInput > 2:                            # preventing input more than or equal 3
                        i = 0
                        while i < 1:
                            try:                                        #this try block preventing value error
                                userInput = int(input('Enter again : '))
                                break
                            except ValueError:
                                i = 0
                    print(matrix[userInput][ci])
                    checkAns(userInput, ci)
                    break
                except ValueError:
                    i = 0
            else:
                break


def userpoints(num):
    global usrpoints
    usrpoints += num
    print('Users points = ', usrpoints, '\n')


def comppoints(num):
    global cmppoints
    cmppoints += num
    print('Computers points = ', cmppoints, '\n')


def checkAns(userIn, computerInput):
    if matrix[userIn][computerInput].lower() == 'w':
        print('Congratulations! You are win. +1 point')
        userpoints(1)
    elif matrix[userIn][computerInput].lower() == 'l':
        print('Sorry! You are lost. Computer win. +1 point')
        comppoints(1)
    else:
        print('Your try has drawn\n')


def addmarks():
    roundnumber = 1
    try:
        open('marks.txt', 'x')
        with open('marks.txt', 'a') as a:
            a.write('Round Number : ' + str(roundnumber))
            a.write('User points = ' + str(usrpoints) + '\n')
            a.write('Computers points = ' + str(cmppoints) + '\n\n')
    except:
        with open('marks.txt', 'r') as r:
            a = r.readlines()
            if len(a) >= 3:
                b = a[-4]
                val = int(b[-2])
            else:
                val = roundnumber - 1
        with open('marks.txt', 'a') as a:
            a.write('Round Number : ' + str(val+1) + '\n')
            a.write('User points = ' + str(usrpoints) + '\n')
            a.write('Computers points = ' + str(cmppoints) + '\n\n')

while True:
    print('Input value should be 0, 1 or 2')
    print('Here,\n 0 represents Snake\n 1 represents Gun\n 2 represnts Water')
    a = input('Do you want to play anymore? press-y or press anykey : ')
    if a.lower() == 'y':
        inputfunc()
    else:
        break

addmarks()