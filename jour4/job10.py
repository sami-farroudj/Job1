def verif(chiffre):
    if type(chiffre)==int:
        print("entier")
    else:print("a virgule")   

    if chiffre%2==0:
        print("pair")
    else: print("impair")

    if chiffre<0:
        print("négatif")
    else:print("positif")

verif(3)
verif(1.5)
verif(2)
