# palíndromo
palabra = input("Inserte una frase")
palabra_rev = palabra[::-1]
if palabra == palabra_rev:
    print("Es palíndromo")
else:
    print("No es palíndromo")
