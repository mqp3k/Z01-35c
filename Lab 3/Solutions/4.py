import random
import os

# 1 - papier
# 2 - kamien
# 3 - nozyce

def clear_console():
    os.system('cls')


def rand_rps():
    rand = random.randint(1,3)
    return rand


def round_res(user_input, pc_input):
    if user_input == '1':
        if pc_input == '1':
            return 'draw'
        elif pc_input == '2':
            return 'win'
        else:
            return 'defeat'

    elif user_input == '2':
        if pc_input == '2':
            return 'draw'
        elif pc_input == '3':
            return 'win'
        else:
            return 'defeat'

    elif user_input == '3':
        if pc_input == '3':
            return 'draw'
        elif pc_input == '1':
            return 'win'
        else:
            return 'defeat'

def num_to_names(num):
    if num == '1':
        return 'Paper'
    elif num == '2':
        return 'Rock'
    else:
        return 'Scissors'

def start_game():
    clear_console()
    print('Rock, Paper, Scissors!')
    print('1. Play the game')
    print('2. Exit')

    inp = '0'

    while inp != '1' and inp != '2':
        inp = input('Select: ')

    if inp == '1':
        clear_console()
        play_game()


def play_game():
    rounds = input("How many round would you like to play?\nYour choice:")
    clear_console()

    (wins, draws, defeats) = (0, 0, 0)

    for r in range(0, int(rounds)):
        print(f'Wins: {wins} \tDraws: {draws} \tDefeats: {defeats} \tRounds Left: {int(rounds) - r}')
        print('1. Paper')
        print('2. Rock')
        print('3. Scissors')

        player_input = 0
        while player_input != '1' and player_input != '2' and player_input != '3':
            player_input = input('Select: ')

        pc_input = str(rand_rps())

        print(f'\nYou: {num_to_names(player_input)} \tVS \tPC: {num_to_names(pc_input)}')
        res = round_res(player_input, pc_input)

        if res == 'win':
            wins = wins + 1
            print('You\'ve won this round!')
        elif res == 'defeat':
            defeats = defeats + 1
            print('You\'ve lost this round!')
        else:
            draws = draws + 1
            print('It\'s a draw this round!')

        input("Press ENTER to continue...")
        clear_console()

    print(f'Wins: {wins} \tDraws: {draws} \tDefeats: {defeats}')

    if wins > defeats:
        print('You\'ve won the game!')
    if defeats > wins:
        print('You\'ve lost the game!')
    elif defeats == wins:
        print('It\'s a draw!')

    input("Press ENTER to continue to main menu...")
    start_game()

if __name__ == "__main__":
    start_game()