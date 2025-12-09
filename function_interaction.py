from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
game_list = ['', 'O', '']

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1, or 2: ')
    return int(guess)
print(player_guess())
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(mylist)

# 1. Amestecă lista
mixed_list = shuffle_list(game_list)

# 2. Ia input de la player
user_guess = player_guess()

# 3. Verifică răspunsul
check_guess(mixed_list, user_guess)
