import random

## Define the Hangman class
class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        # Select a random word from the list
        self.word = random.choice(word_list)

        # Initialise word_guessed with "_"
        self.word_guessed = ['_'] * len(self.word)

        # Calculate number of unique letters in word
        self.num_letters = len(set(self.word))

    
    ## Check whether the guessed letter is in the word
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    #print(index, letter)
                    self.word_guessed[index] = guess
                    print(self.word_guessed)




            #print(f"Good guess! {guess} is in the word.")
            #[index for index, letter in enumerate(self.word) if letter == guess]
            #print(index,letter)


            #self.word_guessed[index] = guess
            #print(self.word_guessed)
            #for letter in self.word:
             #   if letter == guess:
              #      index_letter = self.word.index(letter) 
               #     self.word_guessed[index_letter] = guess
                #    print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")


    # Request user to input a single letter
    def ask_for_input(self):  
        while True:
            guess = input("Please select a letter: ").lower()
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


## Initialise list of favourite fruits and assign to word_list
word_list = ["mango", "strawberry", "peach", "passion fruit", "pineapple"]
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()