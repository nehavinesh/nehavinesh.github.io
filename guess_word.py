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
