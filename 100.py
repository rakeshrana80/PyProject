#!/usr/bin/env python

from datetime import datetime

class century(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print "Name : " + self.name
        print "Age  : " + str(self.age)

    def cen_year(self):
        currentYear = datetime.now().year
        delta = 100 - self.age
        final = currentYear + delta
        return final



alpha = century(raw_input("Enter your name : "),35)
beta = century(raw_input("Enter your name  : "),26)
alpha.display()
beta.display()
Final = alpha.cen_year()
Final1 = beta.cen_year()
print alpha.name + " your 100th year will be %s" %(Final)
print beta.name + " your 100th year will be %s" %(Final1)
