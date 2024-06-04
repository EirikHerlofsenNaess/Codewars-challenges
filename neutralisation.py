# -*- coding: utf-8 -*-

ordbok = {"+-+-" : "--++"}

neutralisation = ""

for a, b in ordbok.items():
    for i in range((len(a)+len(b))//2):
        if a[i] == b[i]:
            neutralisation += a[i]
        else:
            neutralisation+= "0"
    
print(neutralisation)