def triangle(taille):
    for i in range(1,taille):
        print (" "*((taille-i)),end="")
        print("/",end="")
        if i == 1:
            print("\\")
        else:
            print(" "*(2*(i-1)-1), end="")
            print("\\")
    print("/"+"-"*(2*(taille-1)-1)+"\\")
triangle(8)


