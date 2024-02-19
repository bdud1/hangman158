## Import random module
import random 

## Initialise list of favourite fruits and assign to word_list
word_list = ["mango", "strawberry", "peach", "passion fruit", "pineapple"]
# print(word_list)

## Select a random fruit from word_list
word = print(random.choice(word_list))
# print(word)

## Request user to input a single letter
guess = input("Please select a letter: ")


if len(guess) == 1 and guess.isalpha():
    print("Good guess!")