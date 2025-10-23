def moyenne():
    note1=int(input("Entrez votre note1: "))
    note2=int(input("entrez votre note2: "))
    note3=int(input("entrez votre note3: "))
    moyenne_etudiant=(note1+note2+note3)/3
    print(moyenne_etudiant)
    if moyenne_etudiant>=15 :
        print("Très bon élève")
    elif moyenne_etudiant<=14 and moyenne_etudiant >=11:
        print("Bon élève")
    elif moyenne_etudiant <=10 and moyenne_etudiant >=10:
        print("élève moyen")
    elif moyenne_etudiant<8:
        print("élève devant faire des efforts")
moyenne()
