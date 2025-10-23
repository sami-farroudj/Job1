import string
alpha=string.ascii_lowercase
def cesar(message,decalage):
    x= ""
    for i in message:
        x= x + alpha [(alpha.index(i)+decalage)% 26]
    return x
print (cesar("zamo",3))