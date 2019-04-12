import random

word_bank = ["hi", "my", "man", "pizza", "bus", "glasses", "noodles", "computer", "dog", "cat"]
# print(word_bank)

word = random.choice(word_bank)
# print(word)

List_of_letters = list(word)
letters_guessed = []
guesses = 8
win = False

while guesses > 0 and not win:
    # Create the hidden word
    hidden_word = []

    # Take in a guess
    current_guess = input("Type in a letter: ")
    letters_guessed.append(current_guess)

    for letter in word:
        if letter in letters_guessed:
            hidden_word.append(letter)
        else:
            hidden_word.append("*")
    print("".join(hidden_word))


    # Modify Guesses
    if current_guess not in word:
        print("Sorry.")
        guesses -= 1

    if "".join(hidden_word) == word:
        win = True

if win:
    print("You won!")
print("Game end.")
