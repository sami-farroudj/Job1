x= int(input("entrez un entier supèrieur à zéro: "))
while x<=0:
    print("X doit etre supérieiur à zero ")
    x= int(input("entrez un entier supèrieur à zéro: "))
for table in range(1,x+1):
    print(f"table de {table}: ")
    for multiplicateur in range(1,11):
        resultat=table*multiplicateur
        print(F"{table}x{multiplicateur}= {resultat}")