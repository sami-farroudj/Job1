operator=input("choisissez votre operateur: ")
num1=int(input("choisissez un nombre: "))
num2=int(input("choisissez un nombre: "))
def calcule(num1,operator,num2):
    if operator=="+":
        resultat=num1+num2
    elif operator=="-":
        resultat=num1-num2
    elif operator=="/":
        resultat=num1/num2
    return (f'{num1}{operator}{num2}={resultat}')

print(calcule(num1,operator,num2))