#! /usr/bin/env python
#_*_ coding: utf-8 _*_

import os, sys, gnupg, cgi, systemFunctions

def createPGPkey():
    print ("function createPGPkey :)")
    print
    nameUser = raw_input("Entrez votre pseudo : ")

    # Création du dossier contenant les clés
    #os.system('rm -rf /home/miloud/PycharmProjects/PyGPG/gpghome/')
    gpg = gnupg.GPG(gnupghome='lib/gpghome/')
    ########################################

    #Création selon l'identifiant entrées


    varmail = nameUser +"@PGPmail.com"
    varname = nameUser

    #La méthode getpass() permet de masquer l'entrée du mot de passe
    varpass = str(systemFunctions.pass_generator())
    ##############################################################

    #Nous formatons les informations relevées avec la méthode gen_key_input()
    input_data = gpg.gen_key_input(name_real=varname, name_email=varmail, passphrase=varpass, key_length=2048)

    #Nous générons la clé
    key = gpg.gen_key(input_data)
    print 'KEY'
    print key
    ########################

    #nous formatons la variable key en string afin de pouvoir l'utiliser dans la méthode export_keys()
    #key = str(key)
    var = str(varmail)
    key = str(key)

    #Export des clés publiques
    public_keys = gpg.export_keys(key)

    with open(var+'.asc', 'w') as f:
        f.write(public_keys)
    os.system('mv '+var+'.asc lib/publicKeys/')




    #ascii_armored_private_keys = gpg.export_keys(key, True)


    var = varpass
    return var