#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :Sujet_DM_4-Pragassam, Cherif, Mbani-Talamesso, Madikita Bokatola.py
#description     :Ce programe va donne le résultat de la digestion d’une séquence par une enzyme de restriction.
#author          :Anthony PRAGASSAM, Aimen CHERIF, Divine MADIKITA BOKATOLA , Lise MBANI-TALAMESSO
#date            :23/03/20
#version         :1.4
#usage           :python enzyme de restriction.py
#notes           :Dm_Sujet_4, Groupe_4_L2_SDV
#python_version  :3.7.2
#system : windows (Important for winsound module)
#=======================================================================

# Import the modules needed to run the script.
import sys, os, winsound


# Main definition - constants
menu_actions  = {}

# Data
enz =[]  #Valeur où est stockée l'enzyme
siteR=[] #                     les sites de restrictions 
seq=("") #                     la séquence
form=("")#                     la forme de la séquence
ide="false"#Va permettre au programme de savoir si l'enzyme a été entrée corectement
ids="false"#Va permettre au programme de savoir si la séquence a été entrée corectement
idf="false"#Va permettre au programme de savoir si la forme a été entrée corectement
idstop=0   #Va lancer l'arrêt du programme si celui-ci boucle trop

dur=200 #Temps commun pour les beeps des sons de réussites et d'entreés invalides

nbenz=0 #Valeur où est stocké le nombre d'enzyme entrée par l'uttilisateur
siteliste=[] #Valeur où sont stockées les sites de restriction et et la position de coupure de façon séparé (["site",pos])
siteRliste=[] #Valeur où sont stockées les sites de restriction avec leurs positions de coupure(["sit/e"])

id1=0  #Les valeurs idn stockent le nombre de fragment en fonction de la taille de ceux-ci.
id2=0
id3=0  
id4=0
id5=0
id6=0
id7=0
id8=0
id9=0
id10=0
id11=0
id12=0
id13=0
id14=0
id15=0
id16=0
id17=0
id18=0
id19=0
id20=0 #Les valeurs idn stockent le nombre de fragment en fonction de la taille de ceux-ci.
electro="                                                       "#Valeur où sont stockés les traits de migrations
flast="" ##Valeur où est stockée une partie du dernier fragement des séquences circulaires
fter="" #Valeur où est stocké le dernier fragement des séquences circulaire (fter+f1)
aff="" #Valeur où est stocké le choix d'afficher les fragments par l'uttilisateur

# User information
print ("Ce programme va vous permettre de déterminer le résultat de la digestion d’une séquence par une enzyme de restriction (! Seul les enzymes de type II sont prise en compte, référé vous au fichier \"enzyme R2.txt\" ).\n")
print ("Attention: trop de sélection invalide à la suite pour le choix du menu entraine l'arrêt du programme.\n")

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    
    print ("Bienvenu,\n")
    print ("Par quel champ voulez-vous commencer?:,\n")
    print ("1. Choix de l'enzyme de restriction")
    print ("2. Séquence d'ADN (fasta)")
    print ("3. Forme de la séquence")
    print ("4. Execution")
    print ("\n0. Quit") #=>entraine la perte des données entrées
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':# gère le cas où l'utilisateur ne rentre aucune valeur dans le choix du menu
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]() # gère le cas où l'utilisateur entre une bonne valeur dans le choix du menu
        except KeyError:# gère le cas où l'utilisateur entre une valeur éronnée dans le choix du menu
            print ("Selection invalide, recommencez s'il vous plait.\n")
            #winsound.PlaySound("SystemExit", winsound.SND_ALIAS)#Son d'erreur #-- Enlevé car ralenti le programme
            global idstop
            idstop=idstop+1
            if idstop > 2:# A partir de 3 entrées invalides le programme ce stop, Protection mise en place car un bug décrit en dessus n'a pas pu être corrigé et ainsi pour y pallier.
                          #Protection mise en place car si le la séquence entrée possède des sauts de lignes, le programme prend chaque ligne pour un nouvel input dans le choix des menus se qui cause une entrée invalide. Si il y a beaucoup de lignes, le programme va beaucoup boucler sans que l'utilisateur ne puisse rien faire, le seul moyen de l'arrêter est de quitter le programme.
                print ("Arrêt du programme car trop d'erreurs ont été détectées.\nAssurez vous de ne pas avoir entré une séquence avec des sauts de ligne.")
                menu_actions['0']() # entré 0 va faire quitter le programme
                return
            menu_actions['main_menu']()# Va revenir au menu principale
    return

# Enzyme de restriction 1 

def enzyme():
    global idstop
    idstop=0 #Remise à 0 du compteur d'erreur
    global nbenz
    if nbenz==3:
        print ("\nIl n'est possible d'ajouter que 3 enzymes au maximum")
        print ("\n9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return
    global ide
    print ('\nVous êtes dans le menu "Choix d\' une enzyme de restriction"!\n')
    global enz
    enz1=[] # Valeur qui stocke le nom de l'enzyme avant vérification
    enz1=input("Indiquez une enzyme:")
    dictcodon={} #Dictionnaire (qui s'appelle dictcodon) qui stocke le texte dans le fichier
    fh = open ("enzymeR2.txt","r") #Valeur qui va ouvrir le fichier avec les enzymes et sites de restrictions
    for ligne in fh:
        (Enzymes, Sites ) = ligne.split()
        dictcodon[Enzymes] = Sites
    fh.close()

    for i in dictcodon:
        if i==enz1:
            global siteR
            siteR1 = (dictcodon [enz1])# site de restriction
            siteR=siteR1 #Valeur qui va stocker le site de restriction
            nbenz=nbenz+1 #Compteur du nombre d'enzyme
            site=siteR.replace("/","")#Valeur qui va stocker le site de restriction sans le "/"
            g=siteR.find("/") #Valeur qui va stoker la position de coupure "/"
            if g==0: 
                g=1 #empèche que la valeur soit égale à 0 car une position de coupure à 0 bloque le programme

            siteliste.append(site)#Ajout dans la liste du site sans "/"
            siteliste.append(g)#Ajout dans la liste de la position de coupure
            print ("\nEnzyme choisie:",enz1)
            enz.append(enz1)# Liste qui stocke le nom de toutes les enzymes après vérification
            print ("Site de restriction: ",siteR)
            siteRliste.append(siteR)#Ajout dans la liste du site avec "/"
            winsound.Beep(2349,dur,),winsound.Beep(2096,dur),winsound.Beep(3136,dur)#Son de réussite
            
            print ("\nEnzyme valide et enregistée")
            ide="true"#Vérification de l'enzyme

            print ("\n1. Retour au choix de l'enzyme de restriction(pour ajouter une enzyme(rest:",3-nbenz,"))")
            print ("2. Séquence d'ADN (fasta)")
            print ("9. Back(menu)")
            print ("0. Quit")
            choice = input(" >>  ")
            exec_menu(choice)
            return
       
    print ('\nEnzyme "',enz1,'" érronée ou non présente dans la base de donnée.\n')
    winsound.Beep(554,dur,),winsound.Beep(523,700)#Son d'entrée invalide 
    print ("Veuillez retaper ou changer d'enzyme en suivant cette nomenclature:")
    print ("->1ère lettre: genre de la bactérie, en Majuscule (Ex: B )")
    print ("->2ème et 3ème lettres: espèce de la bactérie, en Minuscule (Ex: am )")     #Merci SV42 :)
    print ("->4ème lettre: souche de la bactérie facultatif, en Majuscule (Ex: H )")
    print ("->Chiffre romain: ordre de caractérisation (Ex: I )")
    print ("=>Exemple: BamHI")
    
    print ("\n1. Retour au choix de l'enzyme de restriction")
    print ("9. Back(menu)")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return 


# Séquence d'ADN 2 
def sequence():
    global idstop
    idstop=0 #Remise à 0 du compteur d'erreur
    pos=0 #Initialisation de la positon à 0
    global ids
    print ('\nVous êtes dans le menu "Choix de la séquence ADN"!\n')
    global seq
    seqnot = input(str("Coller ici une séquence d'ADN sans retour à la ligne dans le sens 5'->3'(format FASTA de taille maximal de 100 000 000 caractères):\n"))
    seqnot=seqnot.upper()#Valeur qui stocke la séquence avant vérification
    fasta= ["A" , "T" , "G" , "C"]
    if (len(seqnot)<= 100000000):
        for i in seqnot:
            pos=pos+1 #Compteur qui va noter à quelle position un caractère pose problème
            if (i not in fasta):
                print("\nSéquence invalide car n'est pas au format FASTA(A,T,G,C)")
                print ("Présence du caractère \"", i, "\" en position",pos,"n'est pas prise en compte dans le format FASTA")
                winsound.Beep(554,dur,),winsound.Beep(523,700)#Son d'entrée invalide 
                print ("\nVeuillez retaper ou changer de séquence")
                print ("\n2. Retour au choix de la séquence")
                print ("9. Back(menu)")
                print ("0. Quit")
                choice = input(" >>  ")
                exec_menu(choice)
                return 
        if i in fasta:
            winsound.Beep(2349,dur,),winsound.Beep(2096,dur),winsound.Beep(3136,dur)#Son de réussite
            print("\nSéquence valide et enregistée")
            seq=seqnot #Valeur qui stocke la séquence après vérification
            ids="true"#Vérification de la séquence
            print ("\n3. Forme de la séquence")                                                                                                                                                                                 
            print ("9. Back(menu)")
            print ("0. Quit")
            choice = input(" >>  ")
            exec_menu(choice)
            return
    elif (len(seq)>=100000000):
        print("Séquence invalide car trop longue( plus de 100 000 000 caractères)")
        winsound.Beep(554,dur,),winsound.Beep(523,700)#Son d'entrée invalide
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
    
    

# Forme(linéaire ou circulaire) 3
def forme():
    global idf
    global idstop
    idstop=0 #Remise à 0 du compteur d'erreur
    print ('\nVous êtes dans le menu "forme de la séquence" !\n')
    global form
    formenot = input(str("Quelle est la forme de votre séquence(linéaire ou circulaire)?\n")) #Valeur qui stocke la forme de la séquence avant vérification
    if (formenot == "l") or (formenot == "L") or (formenot == "linéaire") or (formenot == "lineaire") or (formenot == "Linéaire") or (formenot == "Lineaire") :  #on propose plusieurs choix de réponse pour plus de flexibilité dans le programme
        winsound.Beep(2349,dur,),winsound.Beep(2096,dur),winsound.Beep(3136,dur)#Son de réussite
        print("\nForme valide (linéaire) et enregistrée")
        form=formenot #Valeur qui stocke la forme de la séquence après vérification
        form="l"# on enregistre la variable forme sous un nom unique(on a choisi "form" et pas "forme" car le programme le confondait avec la fonction forme se qui bloquait les vérifications.
        idf="true"#Vérification de la forme
        print ("\n9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return
    elif (formenot == "c") or (formenot == "C") or (formenot == "circulaire") or (formenot == "Circulaire"):
        winsound.Beep(2349,dur,),winsound.Beep(2096,dur),winsound.Beep(3136,dur)#Son de réussite
        print("\nForme valide (circulaire) et enregistrée")
        form=formenot
        form="c"# on enregistre la variable forme sous un nom unique
        idf="true"#Vérification de la forme
        print ("\n9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return
    else:
        print ("\nForme invalide, veuillez réessayer avec l, L, linéaire, lineaire, c, C ou circulaire.")
        winsound.Beep(554,dur,),winsound.Beep(523,700)#Son d'entrée invalide
       
    print ("\n3. retour au choix de la forme") #Au début nous voulions que le retour au choix de la "forme" soit automatique lorsqu'on entre une valeur éronnée
                                               #mais cela nous créait une boucle infinie tant qu'on ne rentrait pas une bonne entrée.
    print ("9. Back(menu)")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

#Exécution du programme 4
def execute():
    global id  # Va permettre au programme de savoir si les 3 valeurs ont été entrées correctement pour lancer le traitement des données s'il est a "true"
    id= "false"
    if (enz!=[]) and (seq!="") and (form!=""):
        print ("L'ensemble des données ont été initialisées, prêt à démarrer")
        id=("true")# id=true donc condition validée pour que le programme se lance
    else :
        print ("L'ensemble des données n'ont pas été initialisées")
        winsound.Beep(554,dur,),winsound.Beep(523,700)#Son d'entrée des données invalides
        
   #Va déterminer quelle(s) valeur(s) sont manquante(s) grace aux id        
    if ide=="true" and ids=="true" and idf=="false":# forme
        print ("La forme n'a pas été initialisée")
        print ("\n3. Forme de la séquence")
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return

    elif ide=="false" and ids=="true" and idf=="true":# enzyme
        print ("L'enzyme n'a pas été initialisée")
        print ("\n1. Choix de l'enzyme de restriction")
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return

    elif ids=="false" and ide=="true" and idf=="true":# séquence
        print("La séquence n'a pas été initialisée")
        print ("\n2. Séquence d'ADN (fasta)")
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return

    elif ide=="true" and ids=="false" and idf=="false":# séquence+forme
        print ("La séquence et la forme n'ont pas été initialisées")
        print ("\n2. Séquence d'ADN (fasta)")
        print ("3. Forme de la séquence")
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return

    elif ide=="false" and ids=="true" and idf=="false":# enzyme+forme
        print ("L'enzyme et la forme n'ont pas été initialisées")
        print ("\n1. Choix de l'enzyme de restriction")
        print ("3. Forme de la séquence")
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return
        
    elif ide=="false" and ids=="false" and idf=="true":# enzyme+séquence
        print("L'enzyme et la séquence n'ont pas été initialisées")
        print ("\n1. Choix de l'enzyme de restriction")
        print ("2. Séquence d'ADN (fasta)")
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return

    elif ide=="false" and ids=="false" and idf=="false":# enzyme+séquence+forme
        print("L'enzyme,la séquence et la forme n'ont pas été initialisées")
        print ("\n1. Choix de l'enzyme de restriction")
        print ("2. Séquence d'ADN (fasta)")
        print ("3. Forme de la séquence")
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return

    else :
        winsound.Beep(2349,dur,),winsound.Beep(2096,dur),winsound.Beep(3136,dur)#Son de réussite
        print ("Aucune donnée manquante")
        print ("Press enter to access the program :")
        null=input()#Permet de marquer une pause avant l'exécution

    if id==("true"):
        #Le programme va rappeler les enzymes et site de restriction choisis
        if nbenz==1:
            print ("Enzyme de restriction:",enz[0])
            print ("Site de restriction: ",siteRliste[0])
        elif nbenz==2:
            print ("La 1ère enzyme de restriction est",enz[0],"et sont site de restriction est",siteRliste[0])
            print ("La 2ème enzyme de restriction est",enz[1],"et sont site de restriction est",siteRliste[1])
        elif nbenz==3:
            print ("La 1ère enzyme de restriction est",enz[0],"et sont site de restriction est",siteRliste[0])
            print ("La 2ème enzyme de restriction est",enz[1],"et sont site de restriction est",siteRliste[1])
            print ("La 3ème enzyme de restriction est",enz[2],"et sont site de restriction est",siteRliste[2])
        affseq=input ("\nVoulez-vous afficher la séquence (Non-conseillé pour les longues séquences)?\n☞oui ou non(défault):")
        aff=input ("\nVoulez-vous afficher les fragments triés (Non-conseillé si vous pensez avoir beaucoup de fragments)?\n☞oui ou non(défault):")
        affmigr=input ("\nVoulez-vous afficher la migration sur gel?\n☞oui ou non(défault):")
        
        if affseq=="oui":
            print ("\nSéquence: ",seq)
        if aff=="oui":
            print ("\nLes fragments triés sont:")

        f1="" #Valeur qui stocke le premier fragment en cas de séquence circulaire

        trait="|"
        traitG="│"
        traitGG="▐" #Valeurs qui stockent la taille des chaines de caractère de trait de plus en plus gros
        traitGGG="█"
        témoin=" | | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  " #Valeur qui stocke les traits qui sont l'échelle pour la migration sur gel
        legende=" 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  "#Valeur qui stocke la taille de chaque trait de l'échelle
        flèche="——————————>"
        
        nbfrag=0 #Mise à 0 du nombre de fragment
        
        def digestDNAlinéaire(sequence,rs):
            frags = [] #Valeur où sont stockés les fragments coupés
            last = int(0) #Valeur qui stocke la position du dernier fragment enregistré
            g=""#Valeur qui va intégrer la position en fonction du site de coupure la plus proche
            while 1:
                if nbenz==1:
                    i = sequence.find(rs[0],last)
                    if i == -1:   
                        frags.append(sequence[last:])#Ajout du dernier fragment
                        break
                    else:
                        frags.append(sequence[last:i+rs[1]])#Coupure pour créer les fragments en tenant compte de la position de coupure dans le site de restriction.
                        last = i+rs[1]
                elif nbenz==2:
                    i1 = sequence.find(rs[0],last)
                    i2 = sequence.find(rs[2],last)
                    if (i1==-1): #Choix du site de coupure le plus proche
                        i1=10000000000000000
                    if (i2==-1):
                        i2=10000000000000000
                    if (i1==10000000000000000) and (i2==10000000000000000):
                        i=-1
                    elif (i1<=i2):
                        i=i1
                        g=rs[1]
                    elif (i2<i1):
                        i=i2
                        g=rs[3] #Choix du site de coupure le plus proche
                    if i == -1:
                        frags.append(sequence[last:])#Ajout du dernier fragment
                        break
                    else:
                        frags.append(sequence[last:i+g])
                        last = i+g
                elif nbenz==3:
                    i1 = sequence.find(rs[0], last)
                    i2 = sequence.find(rs[2], last)
                    i3 = sequence.find(rs[4], last)
                    if (i1==-1): #Choix du site de coupure le plus proche
                        i1=10000000000000000
                    if (i2==-1):
                        i2=10000000000000000
                    if (i3==-1):
                        i3=10000000000000000
                    if (i1==10000000000000000) and (i2==10000000000000000) and (i3==10000000000000000):
                        i=-1
                    elif (i1<=i2) and (i1<=i3):
                        i=i1
                        g=rs[1]
                    elif (i2<i1) and (i2<i3):
                        i=i2
                        g=rs[3]
                    elif (i3<i1) and (i3<i2):
                        i=i3
                        g=rs[5] #Choix du site de coupure le plus proche
                    if i == -1:
                        frags.append(sequence[last:])  # Ajout du dernier fragment
                        break
                    else:
                        frags.append(sequence[last:i+g])
                        last = i+g
                   
            return frags
        def digestDNAcirculaire(sequence,rs):
            frags = []#Valeur où sont stockés les fragments coupés
            last = int(0)#Valeur qui stocke la position du derniers fragment enregistré
            g=""#Valeur qui va intégrer la position en fonction du site de coupure la plus proche
            global flast
            while 1:
                if nbenz==1:
                    i = sequence.find(rs[0],last)
                    if i == -1:
                        flast=sequence[last:] #Va stocker le dernier fragment envoyé si la séquence est circulaire qui ne va pas être envoyé pour migration
                        break
                    else:
                        frags.append(sequence[last:i+rs[1]])
                        last = i+rs[1]
                elif nbenz==2:
                    i1 = sequence.find(rs[0],last)
                    i2 = sequence.find(rs[2],last)
                    if (i1==-1): #Choix du site de coupure le plus proche
                        i1=10000000000000000
                    if (i2==-1):
                        i2=10000000000000000
                    if (i1==10000000000000000) and (i2==10000000000000000):
                        i=-1
                    elif (i1<=i2):
                        i=i1
                        g=rs[1]
                    elif (i2<i1):
                        i=i2
                        g=rs[3] #Choix du site de coupure le plus proche
                    if i == -1:
                        flast=sequence[last:]#Va stocker le dernier fragment envoyé si la séquence est circulaire qui ne va pas être envoyé pour migration
                        break
                    else:
                        frags.append(sequence[last:i+g])
                        last = i+g
                elif nbenz==3:
                    i1 = sequence.find(rs[0], last)
                    i2 = sequence.find(rs[2], last)
                    i3 = sequence.find(rs[4], last)
                    if (i1==-1): #Choix du site de coupure le plus proche
                        i1=10000000000000000
                    if (i2==-1):
                        i2=10000000000000000
                    if (i3==-1):
                        i3=10000000000000000
                    if (i1==10000000000000000) and (i2==10000000000000000) and (i3==10000000000000000):
                        i=-1
                    elif (i1<=i2) and (i1<=i3):
                        i=i1
                        g=rs[1]
                    elif (i2<i1) and (i2<i3):
                        i=i2
                        g=rs[3]
                    elif (i3<i1) and (i3<i2):
                        i=i3
                    if i == -1:
                        flast = sequence[last:]# Va stocker le dernier fragment envoyer si la séquence est circulaire qui ne va pas être envoyé pour migration
                        break
                    else:
                        frags.append(sequence[last:i+g])
                        last = i+g

            return frags

        def migrationfrag(taille): #ajout de trait de plus en plus épais pour simuler une migration sur gel 
            global id1
            global id2
            global id3
            global id4
            global id5
            global id6
            global id7
            global id8
            global id9
            global id10
            global id11
            global id12
            global id13
            global id14
            global id15
            global id16
            global id17
            global id18
            global id19
            global id20
            global electro
            if taille<=15:
                if id20==0:
                    electro=electro[:50]+trait+electro[51:]
                    id20=id20+1
                elif id20==1:
                    electro=electro[:50]+traitG+electro[51:]
                    id20=id20+1
                elif id20==2:
                    electro=electro[:50]+traitGG+electro[51:]
                    id20=id20+1
                elif id20==3:
                    electro=electro[:50]+traitGGG+electro[51:]

            elif taille<=30 and taille>15:
                if id19==0:
                    electro=electro[:47]+trait+electro[48:]
                    id19=id19+1
                elif id19==1:
                    electro=electro[:47]+traitG+electro[48:]
                    id19=id19+1
                elif id19==2 :
                    electro=electro[:47]+traitGG+electro[48:]
                    id19=id19+1
                elif id19==3:
                    electro=electro[:47]+traitGGG+electro[48:]
                    
            elif taille<=40 and taille>30:
                if id18==0:
                    electro=electro[:44]+trait+electro[45:]
                    id18=id18+1
                elif id18==1:
                    electro=electro[:44]+traitG+electro[45:]
                    id18=id18+1
                elif id18==2:
                    electro=electro[:44]+traitGG+electro[45:]
                    id18=id18+1
                elif id18==3:
                    electro=electro[:44]+traitGGG+electro[45:]

            elif taille<=50 and taille>40:
                if id17==0:
                    electro=electro[:41]+trait+electro[42:]
                    id17=id17+1
                elif id17==1:
                    electro=electro[:41]+traitG+electro[42:]
                    id17=id17+1
                elif id17==2:
                    electro=electro[:41]+traitGG+electro[42:]
                    id17=id17+1
                elif id17==3:
                    electro=electro[:41]+traitGGG+electro[42:]

            elif taille<=100 and taille>50:
                if id16==0:
                    electro=electro[:38]+trait+electro[39:]
                    id16=id16+1
                elif id16==1:
                    electro=electro[:38]+traitG+electro[39:]
                    id16=id16+1
                elif id16==2:
                    electro=electro[:38]+traitGG+electro[39:]
                    id16=id16+1
                elif id16==3:
                    electro=electro[:38]+traitGGG+electro[39:]
                    
            elif taille<=150 and taille>100:
                if id15==0:
                    electro=electro[:35]+trait+electro[36:]
                    id15=id15+1
                elif id15==1:
                    electro=electro[:35]+traitG+electro[36:]
                    id15=id15+1
                elif id15==2:
                    electro=electro[:35]+traitGG+electro[36:]
                    id15=id15+1
                elif id15==3:
                    electro=electro[:35]+traitGGG+electro[36:]
         
            elif taille<=200 and taille>150:
                if id14==0:
                    electro=electro[:32]+trait+electro[33:]
                    id14=id14+1
                elif id14==1:
                    electro=electro[:32]+traitG+electro[33:]
                    id14=id14+1
                elif id14==2:
                    electro=electro[:32]+traitGG+electro[33:]
                    id14=id14+1
                elif id14==3:
                    electro=electro[:32]+traitGGG+electro[33:]
                    
            elif taille<=250 and taille>200:
                if id13==0:
                    electro=electro[:29]+trait+electro[30:]
                    id13=id13+1
                elif id13==1:
                    electro=electro[:29]+traitG+electro[30:]
                    id13=id13+1
                elif id13==2:
                    electro=electro[:29]+traitGG+electro[30:]
                    id13=id13+1
                elif id13==3:
                    electro=electro[:29]+traitGGG+electro[30:]
                    
            elif taille<=300 and taille>250:
                if id12==0:
                    electro=electro[:26]+trait+electro[27:]
                    id12=id12+1
                elif id12==1:
                    electro=electro[:26]+traitG+electro[27:]
                    id12=id12+1
                elif id12==2:
                    electro=electro[:26]+traitGG+electro[27:]
                    id12=id12+1
                elif id12==3:
                    electro=electro[:26]+traitGGG+electro[27:]
                    
            elif taille<=350 and taille>300:
                if id11==0:
                    electro=electro[:23]+trait+electro[24:]
                    id11=id11+1
                elif id11==1:
                    electro=electro[:23]+traitG+electro[24:]
                    id11=id11+1
                elif id11==2:
                    electro=electro[:23]+traitGG+electro[24:]
                    id11=id11+1
                elif id11==3:
                    electro=electro[:23]+traitGGG+electro[24:]
                    
            elif taille<=450 and taille>350:
                if id10==0:
                    electro=electro[:20]+trait+electro[21:]
                    id10=id10+1
                elif id10==1:
                    electro=electro[:20]+traitG+electro[21:]
                    id10=id10+1
                elif id10==2:
                    electro=electro[:20]+traitGG+electro[21:]
                    id10=id10+1
                elif id10==3:
                    electro=electro[:20]+traitGGG+electro[21:]
                    
            elif taille<=500 and taille>450:
                if id9==0:
                    electro=electro[:17]+trait+electro[18:]
                    id9=id9+1
                elif id9==1:
                    electro=electro[:17]+traitG+electro[18:]
                    id9=id9+1
                elif id9==2:
                    electro=electro[:17]+traitGG+electro[18:]
                    id9=id9+1
                elif id9==3:
                    electro=electro[:17]+traitGGG+electro[18:]
                    
            elif taille<=600 and taille>500:
                if id8==0:
                    electro=electro[:15]+trait+electro[16:]
                    id8=id8+1
                elif id8==1:
                    electro=electro[:15]+traitG+electro[16:]
                    id8=id8+1
                elif id8==2:
                    electro=electro[:15]+traitGG+electro[16:]
                    id8=id8+1
                elif id8==3:
                    electro=electro[:15]+traitGGG+electro[16:]
        
    
            elif taille<=700 and taille>600:
                if id7==0:
                    electro=electro[:13]+trait+electro[14:]
                    id7=id7+1
                elif id7==1:
                    electro=electro[:13]+traitG+electro[14:]
                    id7=id7+1
                elif id7==2:
                    electro=electro[:13]+traitGG+electro[14:]
                    id7=id7+1
                elif id7==3:
                    electro=electro[:13]+traitGGG+electro[14:]
                
            elif taille<=800 and taille>700:
                if id6==0:
                    electro=electro[:11]+trait+electro[12:]
                    id6=id6+1
                elif id6==1:
                    electro=electro[:11]+traitG+electro[12:]
                    id6=id6+1
                elif id6==2:
                    electro=electro[:11]+traitGG+electro[12:]
                    id6=id6+1
                elif id6==3:
                    electro=electro[:11]+traitGGG+electro[12:]
                    
            elif taille<=900 and taille>800:
                if id5==0:
                    electro=electro[:9]+trait+electro[10:]
                    id5=id5+1
                elif id5==1:
                    electro=electro[:9]+traitG+electro[10:]
                    id5=id5+1
                elif id5==2:
                    electro=electro[:9]+traitGG+electro[10:]
                    id5=id5+1
                elif id5==3:
                    electro=electro[:9]+traitGGG+electro[10:]
       
            elif taille<=1000 and taille>900:
                if id4==0:
                    electro=electro[:7]+trait+electro[8:]
                    id4=id4+1
                elif id4==1:
                    electro=electro[:7]+traitG+electro[8:]
                    id4=id4+1
                elif id4==2:
                    electro=electro[:7]+traitGG+electro[8:]
                    id4=id4+1
                elif id4==3:
                    electro=electro[:7]+traitGGG+electro[8:]
                    
            elif taille<=1500 and taille>1100:
                if id3==0:
                    electro=electro[:5]+trait+electro[6:]
                    id3=id3+1
                elif id3==1:
                    electro=electro[:5]+traitG+electro[6:]
                    id3=id3+1
                elif id3==2:
                    electro=electro[:5]+traitGG+electro[6:]
                    id3=id3+1
                elif id3==3:
                    electro=electro[:5]+traitGGG+electro[6:]

            
            elif taille<=2000 and taille>1500:
                if id2==0:
                    electro=electro[:3]+trait+electro[4:]
                    id2=id2+1
                elif id2==1:
                    electro=electro[:3]+traitG+electro[4:]
                    id2=id2+1
                elif id2==2 :
                    electro=electro[:3]+traitGG+electro[4:]
                    id2=id2+1
                elif id2==3 :
                    electro=electro[:3]+traitGGG+electro[4:]

            elif taille>2000:
                if id1==0:
                    electro=electro[:1]+trait+electro[2:]
                    id1=id1+1
                    return
                elif id1==1:
                    electro=electro[:1]+traitG+electro[2:]
                    id1=id1+1
                elif id1==2 :
                    electro=electro[:1]+traitGG+electro[2:]
                    id1=id1+1
                elif id1==3 :
                    electro=electro[:1]+traitGGG+electro[2:]


                    
#############################################################
        if form == "l" :
            liste = [] #initialisation d'une liste vide 
            for fragment in digestDNAlinéaire(seq,siteliste):
                taille = (len(fragment))
                nbfrag=nbfrag+1 #Compteur du nombre de fragments
                liste.append(fragment) #ajout des fragments obtenus dans une liste
                liste.sort(key=lambda item:len(item)) #tri des fragments ,à chaque fois qu'un nouveau fragment est ajouté, par ordre croissant selon la taille en pb
                migrationfrag(taille) #passer les fragments à la migration
            if aff=="oui":
                for i in liste:
                    print (i) #afficher la fragments triés
                    print ("└>La taille du fragment en (pb)est de:",len(i))
            
            print ("\n=>Le nombre de fragement(s) est de:",nbfrag)
            if affmigr=="oui":
                print ("\nEléctrophorèse :")
                print (electro)
                print (témoin)
                print (legende,"☺")
                print(" ")
                print("Interprétation de l'éléctrophorèse :")
                print(" ")
                print("- 20 = fragments inferieur à 15pb ")
                print("- 19 = fragments entre 15 et 30pb " )
                print("- 18 = fragments entre 31 et 40pb " )
                print("- 17 = fragments entre 41 et 50pb " )
                print("- 16 = fragments entre 51 et 100pb " )
                print("- 15 = fragments entre 101 et 150pb " )
                print("- 14 = fragments entre 151 et 200pb " )
                print("- 13 = fragments entre 201 et 250pb " )
                print("- 12 = fragments entre 251 et 300pb " )
                print("- 11 = fragments entre 301 et 350pb " )
                print("- 10 = fragments entre 351 et 450pb " )
                print("- 9 = fragments entre 451 et 500pb " )
                print("- 8 = fragments entre 501 et 600pb " )
                print("- 7 = fragments entre 601 et 700pb " )
                print("- 6 = fragments entre 701 et 800pb " )
                print("- 5 = fragments entre 801 et 900pb " )
                print("- 4 = fragments entre 901 et 1000pb " )
                print("- 3 = fragments entre 1001 et 1500pb " )
                print("- 2 = fragments entre 1501 et 2000pb " )
                print("- 1 = fragments superieur à 2000pb " )


        elif form == "c":
            liste = []#Valeur où sont stockés les fragments triés
            for fragment in digestDNAcirculaire(seq,siteliste):
                taille = (len(fragment))    
                if f1=="":
                    f1=fragment#Stockage du premier fragment qui ne va pas être envoyé pour migration
                else:
                    liste.append(fragment)
                    liste.sort(key=lambda item:len(item))
                    migrationfrag(taille)
            fter=flast+f1 #En cas d'enzyme circulaire, le premier et dernier fragments sont associés dans cette valeur
            migrationfrag(len(fter))
            liste.append(fter)
            liste.sort(key=lambda item:len(item))  #tri des fragments ,à chaque fois qu'un nouveau fragment est ajouté, par ordre croissant selon la taille en pb
            if aff=="oui":
                for i in liste:
                    print (i) #afficher les fragments triés
                    print ("└>La taille du fragment (en pb) est de:",len(i))
           
            print("\n=>Le nombre de fragement(s) est de:",len(liste))  #donne le nombre total de fragments
            if affmigr=="oui":
                print ("\nEléctrophorèse :")
                print (electro)
                print (témoin)
                print (legende,"☻")
                print(" ")
                print("Interprétation de l'éléctrophorèse :")
                print(" ")
                print("- 20 = fragments inferieur à 15pb ")
                print("- 19 = fragments entre 15 et 30pb " )
                print("- 18 = fragments entre 31 et 40pb " )
                print("- 17 = fragments entre 41 et 50pb " )
                print("- 16 = fragments entre 51 et 100pb " )
                print("- 15 = fragments entre 101 et 150pb " )
                print("- 14 = fragments entre 151 et 200pb " )
                print("- 13 = fragments entre 201 et 250pb " )
                print("- 12 = fragments entre 251 et 300pb " )
                print("- 11 = fragments entre 301 et 350pb " )
                print("- 10 = fragments entre 351 et 450pb " )
                print("- 9 = fragments entre 451 et 500pb " )
                print("- 8 = fragments entre 501 et 600pb " )
                print("- 7 = fragments entre 601 et 700pb " )
                print("- 6 = fragments entre 701 et 800pb " )
                print("- 5 = fragments entre 801 et 900pb " )
                print("- 4 = fragments entre 901 et 1000pb " )
                print("- 3 = fragments entre 1001 et 1500pb " )
                print("- 2 = fragments entre 1501 et 2000pb " )
                print("- 1 = fragments superieur à 2000pb " )

            

        winsound.PlaySound("aux_portes_de_la_cite",winsound.SND_FILENAME)#Musique de fin aprés réussite de la migration
    else :
        print("Erreur de données qui ne devrait jamais arriver normalement")#Message d'erreur placé ici pour éviter que le programme ne plante si celui-ci s'avère être vrai mais qui ne devrait pas être possible d'atteindre
        print ("9. Back(menu)")
        print ("0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)
        return
               




# Back to main menu 9
def back():
    menu_actions['main_menu']()#Retour au menu principale

# Exit program 0
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu, #Retour au menu principale
    '1': enzyme,   #Renvoi au choix de l'enzyme
    '2': sequence, #Renvoi au choix de la séquence
    '3': forme,    #Renvoi au choix de de la forme
    '4': execute,  #Lance l'exécution de la migration et des coupures
    '9': back,     #Retour au menu principale
    '0': exit,     #Stop le programme (entraine la perte des données entrées)
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
