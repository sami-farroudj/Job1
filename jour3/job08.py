# a=int(input("choissez une longueur a: "))
# b=int(input("choissez une longueur b: "))
# c=int(input("choissez une longueur c: "))

# if a==b or a==c or b==c:
#     print("isocèle")
# elif a!=b or a!=c or b!=c:
#     print("triangle quelconque")
# elif a**2 + b**2==c and a==b or a==c or b==c:
#     print ("rectangle isocele")
# elif a**2 + b**2==c:
#     print("rectangle")

a= int(input("choisissez une longueur a: "))
b= int(input("choisissez une longueur b: "))
c= int(input("choisissez une longueur c: "))
rectangle = ( a**2+b**2==c**2 or a**2 + c**2==b**2 or b**2+c**2==a**2)
isocele= a== b or a==c or b==c
if rectangle and isocele:
    print("rectangle et isocele")
elif rectangle:
    print("rectangle")
elif isocele:
    print("isocele")
elif a+b<=c or a+c<=b or b+c<=a:
    print("Ce n'est pas un triangle")
else: print("quelconque")