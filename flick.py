# -*- coding: utf-8 -*-


a = ["hei", "flick", "reee", "flick", "opp"]

def flick(liste):
    c = True
    b = []
    for element in liste:
        if element == "flick":
            if c == True:
                c = False
            else:
                c = True
        b.append(c)
    return b

print(flick(a))