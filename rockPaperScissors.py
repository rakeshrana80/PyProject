#!/usr/bin/env python

#Game: Ask for player plays (using input), compare them,
#      print out a message of congratulations to the winner, 
#      and ask if the players want to start a new game
#      Remember the rules:
#
#Rules:
#      Rock beats scissors
#      Scissors beats paper
#      Paper beats rock

import random

machine = ['Rock','Paper','Scissors']
choice = "yes"


def play(mac,human):
    if (mac.lower() == "rock" and human.lower() == "scissors") or (mac.lower() == "scissors" and human.lower() == "paper") or (mac.lower() == "paper" and human.lower() == "rock"):
        print "Computer :{0} Player : {1} ==> Computers Wins!!".format(mac.upper(),human.upper())
    elif (human.lower() == "rock" and mac.lower() == "scissors") or (human.lower() == "scissors" and mac.lower() == "paper") or (human.lower() == "paper" and mac.lower() == "rock"):
        print "Player :{0} Computer :{1} ==> Player Wins!!".format(human.upper(),mac.upper())
    else:
        print "Computer :{0} Player :{1} ==> No Rsults!!".format(mac.upper(),human.upper())

while choice.lower() != "no":
    player_input = raw_input("Enter your choice: " )
    machine_ch = random.choice(machine)
    play(machine_ch,player_input)
    choice = raw_input("Do you want to play again? Enter (Yes/No): ")
    if choice.lower() == "no":
        break

