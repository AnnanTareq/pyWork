import random

exits = False
User_points = 0
computer_points = 0

while exits == False:
    options =['rock', 'paper', 'scissors']
    user_input = input('choose rock, paper, scissors or exit : ')
    comp_input = random.choice(options)

    if user_input == 'exit':
        print('Game ended')
        print('You have won totla score ',User_points,' abd the computer points is ',computer_points)
        exits = True

    if user_input == 'rock':
        if comp_input == 'rock':
            print('Your input is rock')
            print('Computer input rock')
            print('It is a tie')

        elif comp_input == 'paper':
            print('Your input is rock')
            print('Computer input is paper')
            print('Computer wins')
            computer_points += 1

        elif comp_input == 'scissors':
            print('Your input is rock')
            print('Computer input is scissors')
            print('you win')
            User_points += 1

    elif user_input == 'paper':
        if comp_input == 'rock':
            print('Your input is paper')
            print('Computer input is rock')
            print('You win')
            User_points += 1

        elif comp_input == 'paper':
            print('Your input is paper')
            print('Computer input is paper')
            print('its tie')

        elif comp_input == 'scissors':
            print('Your input is paper')
            print('Computer input is scissor')
            print('computer wins')
            computer_points += 1
    elif user_input == 'scissors':
        if comp_input == 'rock':
            print('Your input is scissors')
            print('COmputer input is rock')
            print('computer win')
            computer_points += 1

        elif comp_input == 'paper':
            print('Your input is scissors')
            print('COmputer input is paper')
            print('You win')
            User_points += 1

        elif comp_input == 'scissors':
            print('Your input is scissors')
            print('Computer input is scissors')
            print('its tie')

    elif user_input != 'rock' or user_input != 'paper' or user_input != 'scissors':
        print('Invalid Input')


