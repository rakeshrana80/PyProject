#!/usr/bin/env python

a = [1,3,2,4,3,5,12,12,10,9,15]

new_list = []

num = input("Enter a number: ")

for i in a:
    if i <= num:
        new_list.append(i)


print new_list        

