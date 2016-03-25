#! /usr/bin/env python
#_*_ coding: utf-8 _*_

import os, sys, gnupg, cgi

from functions import cryptFunctions



nameUser = raw_input("Entrez votre pseudo : ")

print cryptFunctions.createPGPkey(nameUser)

