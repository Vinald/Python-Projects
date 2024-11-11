print('Welcome to the Quiz project.\n\n')
choose_quiz_game = int(input('There are two quiz games, choose one (1/2):\n'))


if choose_quiz_game == 1:

    print('Welcome to the quiz game')
    play = input('Do you want to play the game? (y/n): \n')

    if play != 'y':
        quit()

    print('Quiz game started')
    score = 0

    answer = input('What is my name? \n')

    if answer.lower() == 'samuel' or 'vinald' or 'okiror':
        print('Correct answer')
        score += 1

    answer = input('How old am I in 2024 \n')
    if answer == 24:
        print('Correct answer')
        score += 1
        
    answer = input('Who is my best friend?\n')
    if answer.lower() == 'titus':
        print('Correct answer')
        score += 1

    answer = input('are you a python programmer?\n')
    if answer.lower() == 'yes':
        print('Correct answer')
        score += 1

    print(f'You scored {score}')

elif choose_quiz_game == 2:
    def new_game():
        guesses = []
        correct_guesses = 0
        questions_num = 1
        for key in questions:
            print('\n')
            print(key)     
            for i in options[questions_num - 1]:
                print(i)
            questions_num += 1 
            guess = input('Enter A, B, C or D: \n').upper()
            guesses.append(guess)
            correct_guesses += check_answer(questions.get(key), guess)
        questions_num += 1
        display_score(correct_guesses, guesses)

    def check_answer(answer, guess):
        if answer == guess:
            print('corrent!')
            print()
            return 1
        else:
            print('wrong!')
            print()
            return 0

    def display_score(correct_guesses, guesses):
        print('\n')
        print("Results:")
        print('\n')
        print("Answer:", end='')
        for i in questions:
            print(questions.get(i), end=' ')
        print()
        print("Guesses: ", end=' ')
        for i in guesses:
            print(i, end=' ')
        print()
        score = int((correct_guesses/len(questions)) * 100)
        print(f"Score: {score}", end='')

    def play_again():
        response = input("Do you want to play again? (yes or no)").upper()
        if response == 'YES':
            return True
        else:
            return False

    questions = {
        'who created python?': 'A',
        'what year was python created?': 'B',
        'python is tributed to which comedy game?': 'C',
        'Is the earth round?': 'A'
    }

    options = [
        ['A. Guido Van Rosumm', 'B. Elon Musk', 'C. Bill Gates', 'D. John JK'],
        ['A. 1990', 'B. 1991', 'C. 2000', 'D. 1989'],
        ['A. lonlely island', 'B. smosh', 'C. monty python', 'D. SNL'],
        ['A. true', 'B. false', 'C. sometimes', 'D. dont know']
    ]

    new_game()
    print('\n')

    while play_again():
        new_game()

    print('bye')
