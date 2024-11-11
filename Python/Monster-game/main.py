from random import randint

game_running = True
game_results = []


# Menu
def game_menu():
    print('Please select action')
    print('1) Attack')
    print('2) Heal')
    print('3) Exit')
    print('4) Show results')


# calculate attack power of a monster
def cal_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)


# Print the winner
def game_winner(winner):
    print('')
    print('------------------------------------------------')
    print(f'-----------{winner} won the game---------------')
    print('------------------------------------------------')
    print('')


while game_running:
    # Round
    counter = 0
    new_round = True

    # Set parameters for a player and monster
    player = {'name': 'viX', 'attack': 15, 'heal': 16, 'health': 200}
    monster = {'name': 'Max', 'attack_min': 12, 'attack_max': 20, 'health': 200}

    print('Welcome to the Monster Game')
    print('--------------------------')

    # Enter player name
    print('Enter player name')
    player['name'] = input()

    # print player and monster status
    print(f'Player name: {player["name"]} has health {player["health"]}')
    print(f'Monster name: {monster["name"]} has health {monster["health"]}')
    print('--------------------------')

    while new_round:
        counter = counter + 1

        player_won = False
        monster_won = False

        game_menu()
        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']

            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack(monster['attack_min'], monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            print(f'Player healing \n Player health is {player["health"]}')

            player['health'] = player['health'] - cal_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
            for result in game_results:
                print(result)
            print('')

        else:
            print('Invalid Input')

        if not player_won and not monster_won:
            print(f'Monster has health of {monster["health"]} left')
            print(f'Player has health of  {player["health"]} left')

        elif player_won or monster_won:
            new_round = False

            if player_won:
                game_winner(player["name"])
                round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
                game_results.append(round_result)

            elif monster_won:
                game_winner(monster["name"])
                round_result = {'name': monster['name'], 'health': monster['health'], 'rounds': counter}
                game_results.append(round_result)

            else:
                print('Game draw')


print('--------------------------')
print('Game Over')
print('--------------------------')
