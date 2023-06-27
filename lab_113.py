""" Creación de un programa de inventario de vehículos """
import csv
import copy
import random

myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

    myInventoryList = []


""" Copia del archivo CSV en memoria """

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            print(
                f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')

    currentVehicle = copy.deepcopy(myVehicle)

    """ Impresión del inventario de vehículos """
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key, value))
    print("-----")




    """ 114- [PF] - Lab - Condicionales """

    """ Ejercicio 1: Trabajo con la instrucción if """
userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")

    """ Ejercicio 2: Trabajo con la instrucción else """
else:
    print("Please come back when you need to ship a package. Thank you.")





""" 115- [PF] - Lab - Bucles """

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))