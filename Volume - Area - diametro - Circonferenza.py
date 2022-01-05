
"""Capitolo 2 - Programma per calcolare il Diametro, Circonferenza
 Area superficiale e Volume di una sfera mediante l'inserimento del raggio"""

from math import pow
print("""Programma per calcolare Diametro, Circonferenza, Area e Volume di una sfera.
Ora ti chiederò di inserire il raggio.""")
raggio = float(input("Inserisci il raggio: "))

 #diametro  2r
 #circonferenza pigrego x diametro
 #Area superficiale 4 pigrego r alla seconda
 #volume pigrego x cubo raggio x4 /3

Diametro = float(raggio / 2)

Circonferenza =  float(3.14 * Diametro)

Area_superficiale = float((4*3.14) * pow(raggio,2))

Volume = float((pow(raggio,3)*3.14) *4 ) / 3 #Volume

print("Diametro",round(Diametro, 3))
print ("Circonferenza",round(Circonferenza, 3))
print("Area superficiale",Area_superficiale) 
print("Volume", round(Volume, 3))

input("Premi Enter per uscire")
