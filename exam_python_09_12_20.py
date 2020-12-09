from colorama import init 
init()
from colorama import Fore, Back, Style
import random

tours = 0

motATrouver = 0

motAEcrire = [0,1,2,3,4,5,6,7,8,9]
motADeviner = [0,1,2,3,4,5,6,7,8,9]

def choixDuMot (motADeviner[],aleatoire):
    
    aleatoire = 0
    aleatoire = random.randint(0,101)
    print(aleatoire)
    if (aleatoire <=10):
        motADeviner[0] = e
        motADeviner[1] = d
        motADeviner[2] = i
        motADeviner[3] = t
        motADeviner[4] = o
        motADeviner[5] = r
        motADeviner[6] = i
        motADeviner[7] = a
        motADeviner[8] = u
        motADeviner[9] = x
        print(motADeviner)
        return(motADeviner)
    if ((aleatoire <=20) and (aleatoire > 10)):
        motADeviner[0] = o
        motADeviner[1] = s
        motADeviner[2] = t
        motADeviner[3] = e
        motADeviner[4] = o
        motADeviner[5] = p
        motADeviner[6] = a
        motADeviner[7] = t
        motADeviner[8] = h
        motADeviner[9] = e
        print(motADeviner)
        return(motADeviner)
    if ((aleatoire <=30) and (aleatoire > 20)):
        motADeviner[0] = a
        motADeviner[1] = c
        motADeviner[2] = a
        motADeviner[3] = r
        motADeviner[4] = i
        motADeviner[5] = a
        motADeviner[6] = t
        motADeviner[7] = r
        motADeviner[8] = e
        motADeviner[9] = s
        print(motADeviner)
        return(motADeviner)
    if ((aleatoire <=40) and (aleatoire > 30)):
        motADeviner[0] = d
        motADeviner[1] = e
        motADeviner[2] = r
        motADeviner[3] = e
        motADeviner[4] = g
        motADeviner[5] = u
        motADeviner[6] = l
        motADeviner[7] = o
        motADeviner[8] = n
        motADeviner[9] = s
        print(motADeviner)
        return(motADeviner)
    if ((aleatoire <=50) and (aleatoire > 40)):
        motADeviner[0] = d
        motADeviner[1] = i
        motADeviner[2] = v
        motADeviner[3] = i
        motADeviner[4] = s
        motADeviner[5] = e
        motADeviner[6] = r
        motADeviner[7] = a
        motADeviner[8] = i
        motADeviner[9] = s
        print(motADeviner)
        return(motADeviner)
    if ((aleatoire <=60) and (aleatoire > 50)):
        motADeviner[0] = a
        motADeviner[1] = s
        motADeviner[2] = s
        motADeviner[3] = e
        motADeviner[4] = m
        motADeviner[5] = b
        motADeviner[6] = l
        motADeviner[7] = a
        motADeviner[8] = g
        motADeviner[9] = e
        print(motADeviner)
        return(motADeviner)
    if ((aleatoire <=70) and (aleatoire > 60)):
        motADeviner[0] = l
        motADeviner[1] = a
        motADeviner[2] = i
        motADeviner[3] = s
        motADeviner[4] = s
        motADeviner[5] = e
        motADeviner[6] = r
        motADeviner[7] = i
        motADeviner[8] = e
        motADeviner[9] = z
        print(motADeviner)
        return(motADeviner)    
    if ((aleatoire <=80) and (aleatoire > 70)):
        motADeviner[0] = r
        motADeviner[1] = e
        motADeviner[2] = p
        motADeviner[3] = e
        motADeviner[4] = r
        motADeviner[5] = a
        motADeviner[6] = b
        motADeviner[7] = l
        motADeviner[8] = e
        motADeviner[9] = s
        print(motADeviner)
        return(motADeviner)
    if ((aleatoire <=90) and (aleatoire > 80)):
        motADeviner[0] = d
        motADeviner[1] = e
        motADeviner[2] = c
        motADeviner[3] = l
        motADeviner[4] = i
        motADeviner[5] = n
        motADeviner[6] = a
        motADeviner[7] = n
        motADeviner[8] = t
        motADeviner[9] = s
        print(motADeviner)
        return(motADeviner)
    if ((aleatoire <=100) and (aleatoire > 90)):
        motADeviner[0] = i
        motADeviner[1] = n
        motADeviner[2] = d
        motADeviner[3] = e
        motADeviner[4] = x
        motADeviner[5] = a
        motADeviner[6] = t
        motADeviner[7] = i
        motADeviner[8] = o
        motADeviner[9] = n
        print(motADeviner)
        return(motADeviner)    
       

def testLettreRouge(motADeviner, motAEcrire):
    for i in range (motADeviner[0,9]):
        for j in range (motAEcrire[0,9]):
            if (motADeviner[i] = motAEcrire[j]):
                print((Fore.RED + motAEcrire[], end=" ")
    
def testLettreJaune(motADeviner, motAEcrire):
    for i in range (motADeviner[0,9]):
        for j in range (motAEcrire[0,9]):
            if (motADeviner[i] =! motAEcrire[j]):
                 print((Fore.YELLOW + motAEcrire[J], end=" ")
    
    
    
print("Motus")
print("Un mot de 10 lettres a été choisis au hasard, devinez le!")
choixDuMot.motATrouver
while (motAEcrire =! motADeviner) and (tours =!9):
    print("Veuillez entrer la lettre 1")
    motAEcrire[0] =int(input)
    print("Veuillez entrer la lettre 2")
    motAEcrire[1] =int(input)
    print("Veuillez entrer la lettre 3")
    motAEcrire[2] =int(input)
    print("Veuillez entrer la lettre 4")
    motAEcrire[3] =int(input)
    print("Veuillez entrer la lettre 5")
    motAEcrire[4] =int(input)
    print("Veuillez entrer la lettre 6")
    motAEcrire[5] =int(input)
    print("Veuillez entrer la lettre 7")
    motAEcrire[6] =int(input)
    print("Veuillez entrer la lettre 8")
    motAEcrire[7] =int(input)
    print("Veuillez entrer la lettre 9")
    motAEcrire[8] =int(input)
    print("Veuillez entrer la lettre 10")
    motAEcrire[9] =int(input)
    print motAEcrire[]

    testLettreRouge
    testLettreJaune

    tours = tours +1



input()