#!/usr/bin/env python

"""rps.py: A very simple Rock-paper-scissors python console game."""

__author__      = "Carlos Arroyo Villalobos a.k.a Kangu"
__copyright__   = "Copyleft 2017, Heredia, Costa Rica"

import os
from random import randint

class RockPaperScissors:

    OPTIONS_POLL = { 1: 'rock', 2 : 'paper', 3 : 'scissors'}

    wins = 0
    losts = 0
    draws = 0

    exit = 0

    def show_scores(self):
        print("")
        print("Scores:", "wins:", RockPaperScissors.wins,", losts:", RockPaperScissors.losts, ", draws:", RockPaperScissors.draws)

    def show_header(self):
        print("Welcome to a very simple Rock-paper-scissors python console game!")
        print("You will play againt the computer ")

    def options(self):
        print("/********************************/")
        print("Options:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

    def game(self, player, computer):

        print("Player:", RockPaperScissors.OPTIONS_POLL[player])
        print("Computer:", RockPaperScissors.OPTIONS_POLL[computer])

        if player == 1 and computer == 3:
            RockPaperScissors.wins += 1
            print ("You win!")
        elif player == 1 and computer == 2:
            RockPaperScissors.losts += 1
            print ("Computer wins!")
        elif player == 2 and computer == 1:
            RockPaperScissors.wins += 1
            print ("You win!")
        elif player == 2 and computer == 3:
            RockPaperScissors.losts += 1
            print ("Computer wins!")
        elif player == 3 and computer == 1:
            RockPaperScissors.losts += 1
            print ("Computer wins!")
        elif player == 3 and computer == 2:
            RockPaperScissors.wins += 1
            print ("You win!")
        else:
            RockPaperScissors.draws += 1
            print ("Draw")

    def __init__(self):
        self.show_header()
        while RockPaperScissors.exit == 0:

            try:
                self.options()
                player = int(input("Enter a option:"))

                if player > 0 and player < 4:
                    computer = randint(1, 3)
                    self.game(player,computer)
                    self.show_scores()
                    #os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print ("That was no valid option. Try again...")

            except ValueError:
                print ("That was no valid option. Try again...")
                print ("")
            
    pass 

if __name__ == "__main__":
    game = RockPaperScissors()
    


