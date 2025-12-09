# def user_choice():
#     choice ='WRONG'
#     while not choice.isdigit():
#         choice=input('Please enter a number (1-10): ')
#         if not choice.isdigit():
#             print('Sorry that is not a digit value!!')
#     return int(choice)
# user_choice()
from function_interaction import game_list
#
#
def position_choice():
    choice='wrong'
    while choice not in ['0','1','2']:

        choice = input('Pick a position (0,1,2): ')
        if choice not in ['0','1','2']:
            print('Sorry invalid choice!!')
    return int(choice)
position_choice()

def replacement_choice(game_list,position):
    user_placement =input('Type a string to place the position: ')
    game_list[position] = user_placement
    return game_list
replacement_choice(game_list,1)
from IPython.core.display_functions import display


def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y', 'N']:

        choice = input('Keep playing (Y or N): ')
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, plaese choose Y or N !! ")
    if choice == 'Y':
        return True
    else:
        return False
gameon_choice()


game_on = True
game_list=[0,1,2]


def display_game(game_list):
    pass


while game_on:
    display_game(game_list)
    position = position_choice()
    game_list= replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()


