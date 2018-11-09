number = 9
guesses = 5
win = False

while guesses > 0:
    num = int(input("what's a number from 1 to 10?"))
    if num > 11:
        print("it's to high")
        guesses = guesses - 1
    elif num > number:
        print("choose a lower number")
        guesses = guesses - 1
    elif num < number:
        print("a little bit higher")
        guesses = guesses - 1
    elif num == number:
        print("You got it correct!")
        guesses = 0
