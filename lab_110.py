""" Ejercicio 1: Presentar el tipo de dato de cadena """
myString = "This is a string."
print(myString)

print(type(myString))
print(myString + " is of the data type " + str(type(myString)))


""" Ejercicio 2: Trabajar con concatenación de cadenas """
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


""" Ejercicio 3: Trabajar con cadenas de entrada """
name = input("What is your name? ")
print(name)


""" Ejercicio 4: Dar formato a las cadenas de salida """
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))

