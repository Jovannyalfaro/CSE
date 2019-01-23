import random

word_bank = ["hi", "my", "man", "pizza", "bus", "glasses", "noodles", "computer", "dog", "cat"]
# print(word_bank)

word = random.choice(word_bank)
# print(word)

List_of_letters = list(word)
letters_guessed = []
guesses = 8

while guesses > 0:
    # Create the hidden word
    hidden_word = []
    for letter in word:
        if letter in letters_guessed:
            hidden_word.append(letter)
        else:
            hidden_word.append("*")
    print("".join(hidden_word))

    # Take in a guess
    current_guess = input("Type in a letter: ")
    letters_guessed.append(current_guess)

    # Modify Guesses
    if current_guess not in word:
        print("Sorry.")
        guesses -= 1
