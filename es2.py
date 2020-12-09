parole = input("scrivere una lista di parole seguendo questo schema: parola1, parola2, .../n") 
lista1= parole.split(",") 
lista2=[]
for parola in lista1:
 lunghezza=len(parola)
 lista2.append(lunghezza - 1) 
print("la lunghezza delle parole è rispettivamente di", lista2)