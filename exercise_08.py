# Guessing game
# Write a function that takes a number 1 to 9 from the user input (use input function inside a function).
# Store a number in a variable (let’s assume 6). If the input value is less than
# the variable, print (your guess is almost there), if the input value is greater than the variable, print - your guess i

import random

def guessing_number():
    try:
        random_number = random.randint(1, 9)
        user_input = int(input("Enter a number betwwen 1 to 9: "))
        if(user_input<1 and user_input>9):
            print(f"your number : {user_input}, please enter number bwtween 1 to 9")
        else:
            if(random_number>user_input):
                print("your guess is almost there")
            else:
                print(f"your guess: {random_number}")
        
    except ValueError as ve:
        print("please input a valid int number")

guessing_number()