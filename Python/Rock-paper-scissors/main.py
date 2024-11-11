import random


def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f'Computer chose: {computer_choice}')
    print(f'You chose: {user_choice}')

    if user_choice not in choices:
        print('Invalid choice. Please try again.')
        return

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print('You win!')
    else:
        print('Computer wins!')


while True:
    try:
        play_game()
    except Exception as e:
        print(f'An error occurred: {str(e)}')

    play_again = input('Play Again? (yes/no)').lower()
    if play_again != 'yes':
        break
