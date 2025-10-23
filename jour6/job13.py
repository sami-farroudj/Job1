def long(liste):
    compteur = 0
    for _ in liste:
        compteur = compteur+ 1
    return compteur

def supp_double(liste):
    i=0
    while i< long(liste):
        x=0
        doublon_trouve = False
        while x <i:
            if liste[x] == liste[i]:
                del liste[i]
                doublon_trouve = True
                break
            x=x+1
        if not doublon_trouve:
            i=i+1

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
supp_double(L)
print(L)