#!/usr/bin/env python

"""rps.py: A very simple Rock-paper-scissors python console game."""

__author__      = "Carlos Arroyo Villalobos a.k.a Kangu"
__copyright__   = "Copyleft 2017, Heredia, Costa Rica"

import os
from random import randint

#Poll options
ROCK_PAPER_SCISSORS_POLL = { 1: 'rock', 2 : 'paper', 3 : 'scissors'}

def print_option(player, computer):
    print("Player:", ROCK_PAPER_SCISSORS_POLL[player])
    print("Computer:", ROCK_PAPER_SCISSORS_POLL[computer])
 
def rock_paper_scissors(player, computer):

    #Scores
    global wins
    global losts
    global draws
    wins = 0
    losts = 0
    draws = 0

    if player == 1 and computer == 3:
        wins+=1
        return "You win!"
    elif player == 1 and computer == 2:
        losts+=1
        return "Computer wins!"
    elif player == 2 and computer == 1:
        wins+=1
        return "You win!"
    elif player == 2 and computer == 3:
        losts+=1
        return "Computer wins!"
    elif player == 3 and computer == 1:
        losts+=1
        return "Computer wins!"
    elif player == 3 and computer == 2:
        wins+=1
        return "You win!"
    else:
        draws+=1
        return "Draw"

def show_scores():
    print("")
    print("Scores:", "wins:", wins,", losts:", losts, ", draws:", draws)

def main():
    exit = 0
    print("Welcome to a very simple Rock-paper-scissors python console game!")
    print("You will play againt the computer ")
    while exit == 0:
        print("Options:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player = int(input("Enter a option:"))
        computer = randint(1, 3)
        print_option(player, computer)
        print(rock_paper_scissors(player, computer))
        show_scores()
        #os.system('cls' if os.name == 'nt' else 'clear')

main()
    


