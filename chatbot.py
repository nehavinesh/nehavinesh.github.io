# --- Define your functions below! ---
import time


def welcome():
    user_name = input("Hey, I'm chatbot! What's your name?\n ")
    print("Hi", user_name, "nice to meet you")

    return user_name

def joke():
    print("type 'give up' to reveal the answer")
    riddle = input("What do you call a fish with no tail?\n ")
    while riddle != "give up" and riddle != "a dog":
        riddle = input("what do you call a fish with no tail?\n ")
    #if riddle
    else:
        print("A dog :)\n")

def guess_num():
    import random
    num = random.randint(1,101)
    print("I'm thinking of a number between 1 and 100")
    turn = 0
    while turn < 3:
        guess = int(input("What number am I thinking of?\n "))
        if guess > num:
            print("Go lower")
        elif guess < num:
            print("Go higher")
        elif guess == num:
            print("Congrats you got it")
            input("Press enter to exit")
        turn += 1
    if turn == 3:
        if guess > num:
            print("sorry you didn't get it, the number I had in mind was", num)
        elif guess < num:
            print("sorry you didn't get it, the number I had in mind was", num)
        elif guess == num:
            print("Congrats you guess it correctly")
def hangman():
    import random

    #has a set of words and picks one
    words = ["awkward", "croquet", "fishhook", "hyphen", "oxygen","twelfth","ghirardelli"]
    answer = random.choice(words)
    answer = answer.lower()

    #sets all the variables and creates list
    guess = []
    max_fails = 10
    fails = 0
    turns = 0
    gameboard = []


    #prints the gameboard
    print()
    for i in range(len(answer)):
        gameboard.append("_")

    for i in range(len(gameboard)):
        print(gameboard[i], end =" ")
    print()

    #runs until user runs out of guesses
    while fails < max_fails:

        #checks to see if they guessed everything and ends program
        if "_" not in gameboard:
            print("YOU WON!")
            print("It took you", turns, "turns")
            print()
            input("press enter to exit")
            fails = max_fails
            break



        letter = input("guess: ")
    #checks if its a single letter
        if len(letter)>1:
            print("You are only allowed to guess one letter at a time")
            continue

    #checks to see if they already guess it
        if letter not in answer:

            fails += 1
            remaining = max_fails-fails
            print("You have", remaining, "guesses left")
            if remaining == 0:
                print("Game over, the word was", str(answer))
        if letter in guess:
            print ("You have already guessed that")
            continue
        else:
            guess.append(letter)
            turns += 1

        for i in range(len(answer)):
            if letter == answer[i]:
                gameboard[i] = answer[i]
                print("------------------------------------------")
                for i in range(len(gameboard)):
                    print(gameboard[i], end =" ")
                print()
                print("------------------------------------------")

def beemovie():
    from time import sleep
    script = open("beemovie.txt","r")
    for line in script:
        print(line)
        time.sleep(.05)

def user_input(user_name):
    while True:
        print()
        answer = input("Enter 'menu' to see your options.\n ")
        print("enter a number that correpsonds to a choice on the menu")
        if answer == 'menu':
            choice = input('''
1. Hear a joke
2. play Guess the Number
3. play Hangman
4. Bee Movie
''')

            if choice == '1':
                joke()
            if choice == '2':
                guess_num()
            if choice == '3':
                hangman()
            if choice == '4':
                beemovie()
    return choice

def main():
    user_name = welcome()
    answer = user_input(user_name)

main()
