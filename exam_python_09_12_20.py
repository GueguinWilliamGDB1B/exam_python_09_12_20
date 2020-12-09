tours = 0
mot1[b,o,n,j,o,u,r]
mot2[c,h,a,r,p,e,n,t,i,e,r]
mot3[e,s,p,i,o,n]
mot4[s,a,n,g,u,i,n,o,l,a,n,t]
mot5[a,l,p,i,n,i,s,t,e]
mot6[a,u,t,o,m,o,b,i,l,e]
mot7[h,a,b,i,t,u,d,e]
mot8[p,e,r,f,o,r,m,a,n,c,e]
mot9[o,r,d,i,n,a,t,e,u,r]
mot10[c,i,t,r,o,n]




motADeviner = 0
aleatoire = 0

def choixDuMot (motADeviner,aleatoire):
    aleatoire = random.randint(0,101)
    print(aleatoire)
    if (aleatoire <=10):
        motADeviner = mot1
        print(motADeviner)
    if (aleatoire <=20 and aleatoire >10):
        motADeviner = mot2
        print(motADeviner)
    if (aleatoire <=30 and aleatoire >20):
        motADeviner = mot3
        print(motADeviner)
    if (aleatoire <=40 and aleatoire >30):
        motADeviner = mot4
        print(motADeviner)
    if (aleatoire <=50 and aleatoire >40):
        motADeviner = mot5
        print(motADeviner)
    if (aleatoire <=60 and aleatoire >50):
        motADeviner = mot6
        print(motADeviner)
    if (aleatoire <=70 and aleatoire >60):
        motADeviner = mot7
        print(motADeviner)
    if (aleatoire <=80 and aleatoire >70):
        motADeviner = mot8
        print(motADeviner)
    if (aleatoire <=90 and aleatoire >80):
        motADeviner = mot9
        print(motADeviner)
    if (aleatoire <=100 and aleatoire >90):
        motADeviner = mot10
        print(motADeviner)
        
        
        
        
input()