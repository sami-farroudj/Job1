montant_initial= 500
taux_rendement= 3
gain_annuel= montant_initial*taux_rendement / 100
print(f"Gain annuel initial : {gain_annuel: .2f}$")
montant_initial += 5000
taux_rendement +=2
gain_annuel=montant_initial*taux_rendement/ 100
print(f"Après l'augmentation, le nouveau gain annuel est de: {gain_annuel: .2f}$")
retrait = montant_initial* 0.10
montant_initial -= retrait
taux_rendement-= 1
gain_annuel = montant_initial* taux_rendement /100
print(f"Après retrait de 10% et diminution du rendement,montant final : {montant_initial: .2f}$")
print(f"nouveau gain annuel :{gain_annuel: .2f}$")
