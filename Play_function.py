import random
from art import logo
from replit import clear
from Play_function import *


def play():
    print(logo)
    secret_number = random.randint(1, 100)
    level_of_game = input("Want to play game 'Easy' or 'Hard' ?").lower()
    No_of_attempt = 0
    if level_of_game == 'easy':
        No_of_attempt = No_of_attempt + 10
    elif level_of_game == 'hard':
        No_of_attempt = No_of_attempt + 5
    else:
        print('Choose the correct level')
    end_of_game = False

    while not end_of_game:
        guess_no = int(input('Guess a Number'))

        if guess_no == secret_number:
            end_of_game = True
            print('You won')

        elif guess_no < secret_number:
            No_of_attempt -= 1
            print('No u have guessed is Too small')

        elif guess_no > secret_number:
            No_of_attempt -= 1
            print('No u have guessed is Too Big')

        if No_of_attempt == 0:
            end_of_game = True
            print("you have run out of attempt you have lost the Game")
