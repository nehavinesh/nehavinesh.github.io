# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

user_input = input("Type 'left' to go left or 'right' to go right.\n ")

while user_input != "left" and user_input != "right":
    user_input = input("Type 'left' to go left or 'right' to go right.\n ")

if user_input == "left":
    print("You decide to go left and you come to another fork in the road") # Update to match your story.
    user_input = input("Do you wish to go left or right?\n ")
    while user_input != "left" and user_input != "right":
        user_input = input("Type 'left' to go left or 'right' to go right.\n ")
    if user_input == "left":
        print("You choose to go left and it's a dead end. Looks like it's the end of the road for you\n ") # Update to match your story.
        input("Press enter to exit")
    elif user_input == "right":
        print("Congrats, you made it out!!")
        input("press enter to exit")

    # Continue code to finish story.

elif user_input == "right":
    print("You choose to go right and it's a dead end. Looks like it's the end of the road for you\n ") # Update to match your story.
    input("Press enter to exit")

    # Continue code to finish story.
