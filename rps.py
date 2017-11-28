#!/usr/bin/env python

"""rps.py: A very simple Rock-paper-scissors python console game."""

__author__      = "Carlos Arroyo Villalobos a.k.a Kangu"
__copyright__   = "Copyleft 2017, Heredia, Costa Rica"


from random import randint
#print(randint(1, 3))

rock_paper_scissors_poll = { 1: 'rock', 2 : 'paper', 3 : 'scissors'}

def print_option(player, computer):
    print("Player:", rock_paper_scissors_poll[player])
    print("Computer:", rock_paper_scissors_poll[computer])
 
def rock_paper_scissors(player, computer):
    if player == 1 and computer == 3:
        return "You win!"
    elif player == 1 and computer == 2:
        return "Computer wins!"
    elif player == 2 and computer == 1:
        return "You win!"
    elif player == 2 and computer == 3:
        return "Computer wins!"
    elif player == 3 and computer == 1:
        return "Computer wins!"
    elif player == 3 and computer == 2:
        return "You win!"
    else:
        return "Draw"

def main():
    print("Welcome to a very simple Rock-paper-scissors python console game!")
    print("You will play againt the computer ")
    player = 1
    computer = randint(1, 3)
    print_option(player, computer)
    print(rock_paper_scissors(player, computer))

main()
    


