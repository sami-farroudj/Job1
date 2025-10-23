def phare(taille,marche):
    x=(marche*10)*37
    y=x*taille
    tm=y/100
    print(f"pour {marche} marches de {taille} cm, le gardien  parcourt {tm} m par semaine ")

phare(2,12)