# # Game: Rock paper scissors
# # if draw not count
# # 3 rounds each game, win 2 rounds

# options = ['rock','paper','scissors']
# i_win = 0
# computer_win = 0

# import random

# def game():
#     global i_win
#     global computer_win
    
#     my = input('INPUT rock,paper,scissors:').lower()
#     while my not in options:
#         my = input('Please input rock,paper,scissors:').lower()
#     computer = random.choice(options)
#     print(f'Computer plays the {computer.upper()}')
    
#     if my == computer:
#         print('Draw')
#     elif (my == 'rock' and computer == 'scissors') or (my == 'paper' and computer == 'rock') or (my == 'scissors' and computer == 'paper'):
#         print('You Win')
#         i_win += 1
#     else:
#         print('Computer Win')
#         computer_win += 1

#     print(f'You get {i_win}; computer gets {computer_win}') 
#     return i_win, computer_win

# while i_win < 2 and computer_win <2:
#     game()
    
# if i_win == 2:
#     print(f'\nCongratulations')
# else:
#     print(f'\nComputer Win.')  



# v2
import random

def game():
    options = ['rock','paper','scissors']
    i_win = 0
    computer_win = 0

    while i_win < 2 and computer_win <2:
        my = input('INPUT rock,paper,scissors:').lower()

        while my not in options:
            my = input('Please input rock,paper,scissors:').lower()

        computer = random.choice(options)
        print(f'Computer plays the {computer.upper()}')
        
        if my == computer:
            print('Draw')
        elif (my == 'rock' and computer == 'scissors') or (my == 'paper' and computer == 'rock') or (my == 'scissors' and computer == 'paper'):
            print('You Win')
            i_win += 1
        else:
            print('Computer Win')
            computer_win += 1

        print(f'You get {i_win}; computer gets {computer_win}') 
            
    if i_win == 2:
        print(f'\nCongratulations')
    else:
        print(f'\nComputer Win.')  

game()