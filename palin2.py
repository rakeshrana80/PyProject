#!/usr/bin/env python
# palindrome test
# Much simpler way to check for palindrome strings


string = raw_input("Enter a string: ")

if string == string[-1::-1]:
    print "{} is a Palindrome".format(string) 
else:
    print "{} is not a Palindrome".format(string) 

