#!/usr/bin/env python

"""rps.py: A very simple Rock-paper-scissors python console game."""

__author__ = "Carlos Arroyo Villalobos a.k.a Kangu"
__copyright__ = "Copyleft 2017, Heredia, Costa Rica"

import os
from random import randint

class RockPaperScissors:

    OPTIONS_POLL = {1: 'rock', 2: 'paper', 3: 'scissors'}

    def __init__(self):
        self.wins = 0
        self.losts = 0
        self.draws = 0
        self.exit = 0
        # Method of the game
        self.start()

    def show_scores(self):
        print("")
        print("Scores: wins:{0}, losts:{1}, draws:{2}.".format(self.wins, self.losts, self.draws))

    @staticmethod
    def show_header():
        print("Welcome to a very simple Rock-paper-scissors python console game!")
        print("You will play against the computer ")

    @staticmethod
    def options():
        print("/********************************/")
        print("Options:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

    def game(self, player, computer):

        print("Player:", RockPaperScissors.OPTIONS_POLL[player])
        print("Computer:", RockPaperScissors.OPTIONS_POLL[computer])

        if player == 1 and computer == 3:
            self.wins += 1
            print("You win!")
        elif player == 1 and computer == 2:
            self.losts += 1
            print("Computer wins!")
        elif player == 2 and computer == 1:
            self.wins += 1
            print("You win!")
        elif player == 2 and computer == 3:
            self.losts += 1
            print("Computer wins!")
        elif player == 3 and computer == 1:
            self.losts += 1
            print("Computer wins!")
        elif player == 3 and computer == 2:
            self.wins += 1
            print("You win!")
        else:
            self.draws += 1
            print("Draw")

    def start(self):
        self.show_header()
        while self.exit == 0:

            try:
                self.options()
                player = int(input("Enter a option:"))

                if player > 0 and player < 4:
                    computer = randint(1, 3)
                    self.game(player, computer)
                    self.show_scores()
                    # os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print("That was no valid option. Try again...")

            except ValueError:
                print("That was no valid option. Try again...")
                print("")


if __name__ == "__main__":
    game = RockPaperScissors()
    


