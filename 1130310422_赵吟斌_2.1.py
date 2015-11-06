# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:19:31 2013

@author: Kimi
"""

# question 1
sum=0
for x in range(1,1000):
    if x%3==0 or x%5==0:
        sum=sum+x
print sum    
print sum


# question 2
# define a function to test prime number

import math
s=0
def rx(y):
   a=2   
   t=int(math.sqrt(y))
   while a<=t:
       if  y%a==0:
           return False
       else:
           a=a+1
   return True

# calculate the sum of these prime number from 1 to 2000000
for y in range(2,2000000):
    if rx(y):
       s=s+y
print s  #answer s is right,but over time



# question3
# check year
def leapyear(y):
    if y%400==0 or (y%4==0 and y%100!=0):
        return True
    else:
        return False

m1=m3=m5=m7=m8=m10=m12=31
m4=m6=m9=m11=30
s=0         
days=1
dly=[m1,29,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]  # days in every months of leap years
dny=[m1,28,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]  # days in every months of normal years

for y in range(1901,2001):
    if leapyear(y):
        for x in dly:
            days=days+x
            if days%7==5:
                s=s+1
                
    else:
        for x in dny:
            days=days+x           
            if days%7==5:
                s=s+1
print s
print "soft"
