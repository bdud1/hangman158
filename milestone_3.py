# Request user to input a single letter
guess = input("Please select a letter: ")
while True:
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character: ")


 