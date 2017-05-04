#!/usr/bin/env python

#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether 
#they guessed too low, too high, or exactly right.

import random,sys


def main():
    rand_number = random.randint(1,9)
    count = 0
    choice = "yes"
    while choice.lower() != "no":
        guess = input("Guess the Magic Number between 1 and 9 : ")
        if guess == rand_number:
            count += 1
            print "You guessed the correct nmber {0} in {1} attempts : WINNER !!!".format(rand_number,count)
            count = 0
            sys.exit()
        elif guess > rand_number:
            count += 1 
            print "You have guessed too high, sorry try again !"
            choice = raw_input("Do you want to guess again? (Yes/No) :")   
        else:
            count += 1 
            print "You have guessed too low, sorry try again !"
            choice = raw_input("Do you want to guess again? (Yes/No) :")   

if __name__ == "__main__":
    main()
