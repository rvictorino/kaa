#! /usr/bin/env python
#_*_ coding: utf-8 _*_

import os, sys, gnupg, cgi

from functions import cryptFunctions


print("BIENVENUE SUR KAA")
print("-----------------")
choice = raw_input ("1 pour creer un utilisateur | 2 pour choisir son interlocuteur")

if(choice == 1):
    print cryptFunctions.createPGPkey()

elif(choice == 2):
    print ("interlocuteur")




