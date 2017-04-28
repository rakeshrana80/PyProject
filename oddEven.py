#!/usr/bin/env python

class OddEven(object):
    def __init__(self,num):
        self.num = num

    def numCheck(self):
        if (int(self.num) % 2) == 0:
            return "EVEN"
        else:
            return "ODD"


number = OddEven(input("Enter a number : "))
result = number.numCheck()
print "Number you entered is %s" %(result)
