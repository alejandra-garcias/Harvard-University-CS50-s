
from random import randint, choice

def choose_word(word_list):
    chosen_word = choice(word_list)
    unique_letters = len(set(chosen_word))
    return chosen_word, unique_letters

def display_word(word, correct_letters):
    result = [letter if letter in correct_letters else '-' for letter in word]
    print(' '.join(result))

def ask_letter():
    letter = ''
    valid_letter = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not valid_letter:
        letter = input('Choose a letter: ').lower()
        if letter in alphabet and len(letter) == 1:
            valid_letter = True
        else:
            print('Invalid letter. Please try again.')

    return letter

def check_letter(letter, word, attempts, correct_guesses, unique_letters, correct_letters, incorrect_letters):
    finished = False
    if letter in word:
        correct_letters.add(letter)
        correct_guesses += 1
    elif letter not in incorrect_letters:  # Check if the letter is not already guessed incorrectly
        incorrect_letters.add(letter)
        attempts -= 1

    if attempts == 0:
        finished = lose_game(word)
    elif correct_guesses == unique_letters:
        finished = win_game(word, correct_letters)

    return attempts, finished, correct_guesses

def lose_game(word):
    print('Out of attempts! The word was:', word)
    return True

def win_game(word, correct_letters):
    display_word(word, correct_letters)
    print("Congratulations, you've guessed the word!")
    return True

def generate_math_question():
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    operation = choice(['+', '-', 'x', '/'])
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == 'x':
        answer = num1 * num2
    elif operation == '/':
        # Ensure a valid division problem with a whole number result
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        answer = num1 * num2
    
    problem = f"{num1} {operation} {num2}"
    return problem, answer

def play_math_game():
    score = 0
    attempts = 5

    print("Welcome to the Math Game!")
    print("Answer the following math problems. You have 5 attempts.")

    for _ in range(5):
        problem, correct_answer = generate_math_question()
        print(f"\nProblem: {problem}")
        
        user_answer = input("Your answer: ")
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
            attempts -= 1

        if attempts == 0:
            print("You've run out of attempts. Game over.")
            break

    print(f"\nMath Game Over. Your score: {score}/5")
    return score

    return score >= 3  # Player needs at least 3 correct answers to win

def play_hangman():
    words = [
        "python", "programming", "computer", "development", "learning",
        "technology", "intelligence", "data", "algorithm", "cycle",
        "conditional", "variable", "function", "dictionary", "iteration",
        "class", "module", "string", "index", "method"
    ]

    word, unique_letters = choose_word(words)
    attempts = 6
    correct_guesses = 0
    correct_letters = set()
    incorrect_letters = set()

    game_over = False

    while not game_over:
        print('\n' + '*' * 20 + '\n')
        display_word(word, correct_letters)
        print('\n')
        print('Incorrect letters: ' + '-'.join(incorrect_letters))
        print(f'Attempts left: {attempts}')
        print('\n' + '*' * 20 + '\n')

        letter = ask_letter()
        attempts, game_over, correct_guesses = check_letter(
            letter, word, attempts, correct_guesses, unique_letters, correct_letters, incorrect_letters
        )

    return correct_guesses == unique_letters

def play_trivia():
    print("\n*** Trivia Game ***")
    question = generate_trivia_question()
    print(question)
    answer = input("Enter 'yes' or 'no': ").lower()

    if check_trivia_answer(question, answer):
        print("Correct! You earned a point.")
        return True
    else:
        print("Incorrect. No point earned.")
        return False

def generate_trivia_question():
    trivia_questions = [
        "Is the Earth flat?",
        "Is the capital of France London?",
        "Is Python a programming language?",
        "Was Leonardo da Vinci a famous painter?",
        "Is the sun a planet?"
    ]
    return choice(trivia_questions)

def check_trivia_answer(question, answer):
    correct_answers = {
        "Is the Earth flat?": "no",
        "Is the capital of France London?": "no",
        "Is Python a programming language?": "yes",
        "Was Leonardo da Vinci a famous painter?": "yes",
        "Is the sun a planet?": "no"
    }
    return answer == correct_answers.get(question, "no")

def main():
    print("Welcome to the Game Center!")

    while True:
        print("\nSelect a game:")
        print("1. Hangman")
        print("2. Trivia")
        print("3. Math Game")
        print("4. Quit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            if play_hangman():
                print("You win!")
            else:
                print("You lose!")

        elif choice == "2":
            play_trivia()

        elif choice == "3":
            if play_math_game():
                print("You win!")
            else:
                print("You lose!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
