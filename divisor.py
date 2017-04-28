#!/usr/bin/env python


divisors = []
num = input("Enter a number of your choice: ")

for i in range(2,num):
    if (num % i ) == 0:
        divisors.append(i)



print "Divisors of %s are %s" %(num,divisors)

