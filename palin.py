#!/usr/bin/env python
# palindrome test

import sys

string = raw_input("Enter a string: ")
print string

length = len(string)
print length

# check for palindrum
mid = length / 2

j = -1
for i in range(mid):
    if string[i] == string[j]:
        j -= 1
        continue
    else:
        print "{} is not a palindrome".format(string)
        sys.exit(1)
         

print "{} is a palindrome ".format(string)    

