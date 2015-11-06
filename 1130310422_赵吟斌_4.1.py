# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:50:48 2013

@author: Administrator
"""

def pl(i):
    if i[0] in ["a","e","i","o","u"]:
        i = i + "hay"
        return i
    if i[:2] == "qu":
        i = i[2:] + "quay"
        return i
    else:
        n = len(i)
        index = 1    
        while index < n:                            
            if not i[index] in ["a","e","i","o","u","y"]:                                      
                index = index + 1
            else:
                break
        i = i[index:] + i[:index] + "ay"    
    return i

word=raw_input()
a=str.split(str.lower(word))
t=""
for i in a:
    t=t+str(pl(i))+" "
print t[:-1]