def ferme(type,saison):
    if type=="fruits" and saison=="hiver":
        print("orange,mandarine et kiwi")
    
    elif type=="fruits" and saison=="été":
        print("poire,fraise,cassis")
    
    elif type=="légume" and saison=="hiver":
        print('carotte,topinambour,endive')
    
    elif type=="légume" and saison=="été":
        print("artichaut,aubergine,navet")
ferme("légume","hiver")
ferme("fruits","été")