# Rock Paper Scissors Game

# -----PSUEDO CODE-----#

# TWO MAIN VARIABLES: PLAYER AND COMPUTER(RANDOM)
# COMPUTER HAS 3 RANDOM OPTIONS (ROCK, PAPER, SCISSORS)
# PLAYER'S DECISION IS COMPLETED BY AN INPUT STATEMENT

# PRINT RULES OF PLAY:
# ROCK VS PAPER | PAPER WINS
# ROCK VS SCISSORS | ROCK WINS
# PAPER VS SCISSORS | SCISSOR WINS


# ---global variables below ---#
# DEFAULT LIST TO STORE THE 3 OPTIONS
# GAME_CHOICES = ["ROCK", "PAPER", "SCISSORS"]
# WIN/LOSE COUNTER(?)

# OPTION TO START OR END THE GAME?(while True)

# CONDITIONS THAT CAN BE MET DURING GAME PLAY:
# IF PLAYER == ROCK AND COMPUTER == PAPER:
# SHOW PLAYER LOSES
# IF PLAYER == SCISSORS AND COMPUTER == ROCK:
# SHOW PLAYER LOSES
# IF PLAYER == PAPER AND COMPUTER == SCISSORS:
# SHOW PLAYER LOSES
# ELSE:
# PLAYER WINS

# CONTINUE TO ASK PLAYER FOR INPUT UNTIL THEY PRESS 'Q' TO QUIT.
# IF RESPONSE.LOWER(ACCOUNTS FOR UPPER CASE INPUT) == 'Q':
# PRINT ("THANK YOU FOR PLAYING")
# BREAK


# import random module
from random import randint

# welcome to rock, paper scissors and general instructions
print("\nWelcome to the Rock, Paper, Scissors Game")
print("Made in 2023 by Kenai and Priscilla")

# display the rules of the game
print("\n\t------------| Rules of the game: |-------------")
print("\tRock vs Paper | PAPER WINS\n\tRock vs Scissors | ROCK WINS\n\tPaper vs Scissors | SCISSORS WIN")

# keep track of user wins and computer wins
# defaults to 0
player_win_count = 0
computer_win_count = 0
draw_count = 0

# start the game using while False

while True:
    player = input("Please pick from these options: Rock, Paper, Scissors: ")

    # list of choices - can only be "Rock", "Paper", or "Scissors"
    gameplay_options = ["Rock", "Paper", "Scissors"]
    computer = gameplay_options[randint(0, 2)]

    # print what player chose
    print("You chose: " + player)
    print("Computer chose: " + computer)
