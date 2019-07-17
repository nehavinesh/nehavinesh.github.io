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
