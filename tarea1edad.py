#Edad del individuo más viejo
nom1 = input("Inserte el nombre del primer ind ")
nom2 = input ("Inserte el nombre del segundo ind ")
edad1 = input ("Inserte edad del primer ind ")
edad2 = input ("Inserte edad del segundo ind ")
if edad1 > edad2:
    print("El individuo de mayor edad es: {}" .format(nom1))
    print("Su edad es: {}".format(edad1))
elif edad1 == edad2:
    print("Los individuos son de la misma edad")
else:
    print("El individuo de mayor edad es: {}" .format(nom2))
    print("Su edad es: {}".format(edad2))
