def long(liste):
    compteur= 0
    for _ in liste:
        compteur = compteur + 1
    return compteur

def trier_liste(liste):
    x=long(liste)
    for i in range(x):
        for n in range(0,x-i-1):
            if liste[n]> liste[n+1]:
                liste[n],liste[n+1]= liste[n+1],liste[n]

    return liste 
la_liste = [30,10,42,11,6]
print(trier_liste(la_liste))

