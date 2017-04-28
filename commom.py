#!/usr/bin/env python

import random

x = random.sample(range(100),10)
y = random.sample(range(20),15)
comm = []

print "X : {}".format(x)
print "Y : {}".format(y)

for i in x:
    if i in y and i not in comm:
        comm.append(i)
print comm

# second method

a = set([1,1,2,3,5,8,13,21,34,55,89])
b = set([1,2,3,4,5,6,7,8,9,10,11,12,13])

print "a: {0} \nb: {1}".format(a,b)
print "In common elements = {}".format(a&b)
