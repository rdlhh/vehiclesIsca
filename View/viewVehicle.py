import controllerVehicle
from vehicleapi import getDistance

controller = controllerVehicle.ControllerVehicle()

def readPlate():
    plate=""
    while(True):
        plate = input("Enter the plate: ")
        if(len(plate) == 7):
            numPart = plate[0:4]
            lettersPart = plate[4:]
            if(numPart.isdigit()):
                if(lettersPart.isalpha()):
                    break
        print("ERROR entering the plate.")
    return plate

def addVehicle():
    plate = readPlate()
    desc = input("Enter description: ")
    while(True):
        chasis = input("Enter chasis (17 characters): ")
        if(len(chasis) == 17):
            break
        print("ERROR entering the chasis (17 characters)")
    driver = input("Enter the driver name: ")
    if(controller.addVehicle(plate, desc, chasis, driver)):
        print("Vehicle add succesfully!")
    else: print("ERROR adding the vehicle, plate already exists.") 

def delVehicle():
    plate = readPlate()
    if(controller.deleteVehicle(plate)):
        print("Vehicle deleted!")
    else:
        print("ERROR deleting vehicle")

def addOdometer():
    plate = readPlate()
    date = input("Enter date [dd/mm/aaaa]")
    fromCity = input("From: ")
    destCity = input("To: ")
    kms = getDistance(fromCity, destCity)/1000
    if(controller.addOdometer(plate, date, fromCity, destCity, kms)):
        print("Odometer added succesfully!")
    else:
        print("Error adding odometer")

def listVehicles():
    vehicles = controller.getVehicles()
    for plate,vehicle in vehicles.items():
        print("Plate: ", plate)
        print("Description: ", vehicle.getDesc())
        print("Chasis: ", vehicle.getChasis())
        print("Driver: ", vehicle.getDriver())
        print("Unconfirmed odometer")
        for date, odometer in vehicle.getOdometer().items():
            print("\t", date, odometer[0], odometer[1], odometer[2])

def confirmOdometer():
    plate = readPlate()
    date = input("Enter date [dd/mm/aaaa]")
    if(controller.confirmOdometer(plate, date)):
        print("Correct confirm odometer!")
    else:
        print("Error confirm odometer!")

while(True):
    print("Currently there are ", controller.getNumberOfVehicles(), " vehicles registered!")
    print("1.- Add a vehicle")
    print("2.- Delete vehicle")
    print("3.- Add odometer")
    print("4.- Confirm odometer")
    print("5.- List vehicle")
    print("6.- Exit")
    option = int(input("Choose option: "))

    if(option == 6 ):
        print("BYE")
        break
    elif(option == 1):
        addVehicle()
    elif(option == 2):
        delVehicle()
    elif(option == 3):
        addOdometer()
    elif(option == 4):
        confirmOdometer()
    elif(option == 5):
        listVehicles()