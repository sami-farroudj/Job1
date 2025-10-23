L=[8,24,27,48,2,16,9,7,84,91]
somme=0
for pair in L:
    if pair%2==0:
        somme+=pair
print(somme)