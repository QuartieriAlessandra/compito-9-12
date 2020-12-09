parola=input ("scrivere la parola da processare:")
parola1 =parola [::-1] 
if parola == parola1:
 print(parola, "è un polindromo")
else:
 print(parola, "non è un palindromo")