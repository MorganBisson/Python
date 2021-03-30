pSeuil = 2.3
vSeuil = 7.41

p = float(input("La pression : "))
v = float(input("Le volume courant : "))
 
if p > pSeuil and v > vSeuil:
    print("Arrêt immédiat")
elif p > pSeuil:
    print("Augmenter le volume de l'enceinte")
elif v > vSeuil:
    print("Augmenter le volume de l'enceinte")
else: 
    print("tout va bien")