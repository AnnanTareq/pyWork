import random


def roll_dice():

    dice_drawing = {
       1:(
           "--------------",
           "|         1  |",
           "|     0      |",
           "|            |",
           "|____________|",
       ),
       2:(

           "--------------",
           "|  0      2  |",
           "|            |",
           "|         0  |",
           "|____________|",
       ),
       3 :(

           "--------------",
           "| 0       3  |",
           "|     0      |",
           "|         0  |",
           "|____________|",
       ),
       4:(

           "--------------",
           "|  0       0  |",
           "|      4      |",
           "|  0       0  |",
           "|_____________|",
       ),
       5:(

           "--------------",
           "| 0       0  |",
           "|     0      |",
           "| 0   5   0  |",
           "|____________|",
       ),
       6:(
           "--------------",
           "| 0       0  |",
           "| 0    6  0  |",
           "| 0       0  |",
           "|____________|",
       )

   }

    roll = input('Roll the dice? Yes/No : ')

    while roll.lower() == 'Yes'.lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1, 6)

        print('dice rolled: {} and {}'.format(dice1, dice2))
        print(''.join(dice_drawing[dice1]))
        print(''.join(dice_drawing[dice2]))

        roll = input('Roll again? Yes/No:')


roll_dice()