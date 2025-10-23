nom_produit="crayon"
prix_unitaire= 1.5
quantite_stock = 50
print(f"produit : {nom_produit}")
print(f"prix unitaire : {prix_unitaire: .2f}")
print(f"quantité en stock:{quantite_stock}")
quantite_achetee = int(input("Combien de produits souhaitez vous acheter?"))
if quantite_achetee > quantite_stock:
    print("Désolé, nous n'avons pas assez de stock pour cette quantité.")
else:
    quantite_stock -= quantite_achetee
    print(f"merci pour votre achat de {quantite_achetee} {nom_produit}.")
    print(f'stock restant : {quantite_stock}')
    prix_unitaire *= 1.10
    print(f"suite a l'inflation, le prix est maintenant de : {prix_unitaire : .2f} $")