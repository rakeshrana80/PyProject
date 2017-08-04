#!/usr/bin/env python
# Author: Rakesh Rana
# Date: 2017-08-04
#
#####################

import sys
import os

board = [" " for x in range(0,9)]


# displaying the board 
def display_board():
    print "{} | {} | {}".format(board[0],board[1],board[2])
    print "----------"
    print "{} | {} | {}".format(board[3],board[4],board[5])
    print "----------"
    print "{} | {} | {}".format(board[6],board[7],board[8])

# Players move function
def player_move(icon):
    while True:
        if icon == 'X':
            pos=input("==> Player1: choose a position from 1 to 9: ")
            if board[pos -1] == " ":
                board[pos - 1] = icon
                break
            else:
                print "Position already taken, Please choose a different postion..."
                continue
        elif icon == 'O':
            pos=input("==> Player2: choose a position from 1 to 9: ")
            if board[pos -1] == " ":
                board[pos - 1] = icon
                break
            else:
                print "Position already taken, Please choose a different postion..."
                continue

# check for any winner
def check4winner(icon):
    if ( board[0] == board[1] == board[2] == icon or board[3] == board[4] == board[5] == icon or board[6] == board[7] == board[8] == icon or board[0] == board[3] == board[6] == icon or board[1] == board[4] == board[7] == icon or board[2] == board[5] == board[8] == icon or board[0] == board[4] == board[8] == icon or board[2] == board[4] == board[6] == icon ):
        display_board()
        print " "
        print "++++++++++++++++++++++++++"
        print "|  {} is winner!!!  |".format("Player1" if icon == 'X' else "Player2")
        print "++++++++++++++++++++++++++"
        print " "
        sys.exit(1)


def main():
    while True:
        for mov in ['X','O']:
            os.system("clear")
            check4winner(mov)
            display_board()
            player_move(mov)

# calling the main function
if __name__ == '__main__':
    main()
