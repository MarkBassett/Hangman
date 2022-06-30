import random


class Hangman:
    def __init__(self):
        self.user_guess = None
        self.words = ['python', 'java', 'swift', 'javascript']
        self.word = random.choice(self.words)
        self.word_set = set(self.word)
        self.user_guesses = set()
        self.attempts = 8
        self.game_result = 'You lost!'
        self.start_position()


    def start_position(self):
        self.user_guess = ['-' for l in self.word]
        print(f'H A N G M A N  # {self.attempts} attempts')

    def display_word(self):
        print()
        print(''.join(self.user_guess))

    def game_won(self):
        if len(self.word_set) == 0:
            self.game_result = 'You survived!'
            self.attempts = 0
            print(f'You guessed the word {self.word}!')

    def validate_input(self, letter):
        if len(letter) != 1:
            print('Please, input a single letter.')
            return False
        elif letter.isupper() or not letter.isalpha():
            print('Please, enter a lowercase letter from the English alphabet.')
            return False
        elif letter in self.user_guesses:
            print("You've already guessed this letter.")
        self.user_guesses.add(letter)
        return True

    def game(self, guess):
        if self.validate_input(guess):
            if guess in self.word_set:
                self.word_set.discard(guess)
                for i, l in enumerate(self.word):
                    if l == guess:
                        self.user_guess[i] = guess
            else:
                if guess not in self.word:
                    self.attempts -= 1
                    print("That letter doesn't appear in the word.", end=' ')
                elif guess in self.user_guess:
                    self.attempts -= 1
                    print('No improvements.')
                print(f'# {self.attempts} attempts')
        self.display_word()
        self.game_won()

    def game_analysis(self, guess):
        if guess == self.word:
            print('You survived!')
        else:
            print('You lost!')

win_no = 0
loss_no = 0
while True:
    hangman = Hangman()
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    menu_option = input()
    if menu_option == 'results':
        print(f'You won: {win_no} times')
        print(f'You lost: {loss_no} times')
    elif menu_option == 'exit':
        break
    else:
        hangman.display_word()
        while hangman.attempts > 0:
            hangman.game(input('Input a letter: '))
        if hangman.game_result == 'You survived!':
            win_no += 1
        else:
            loss_no += 1
        print(hangman.game_result)
