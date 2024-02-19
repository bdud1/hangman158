## Import random module
import random 

## Initialise list of favourite fruits and assign to word_list
word_list = ["mango", "strawberry", "peach", "passion fruit", "pineapple"]
# print(word_list)

## Select a random fruit from word_list
word = random.choice(word_list)
print(word)

# Request user to input a single letter
guess = input("Please select a letter: ")
while True:
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character: ")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
 