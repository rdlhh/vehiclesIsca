import controllerAirport
from airportApi import getAirport

controller = controllerAirport.ControllerAirport()

def addAirport():
    iata = input("Enter IATA")
    getAirport()
        


while(True):
    print("AIRPORT DATABASE")
    print("---------------------------")
    print("1.- Import an airport")
    print("2.- Delete an airport")
    print("3.- Add a flight operator to an airport")
    print("4.- DElete a flight operator to an airport")
    print("5.- List airports by operators")
    print("6.- List number of planes by operator - (by airport / all)")
    print("7.- Exit")
    option = int(input("Choose option: "))

    if(option == 7):
        print("BYE!")
        break
    elif(option == 1):
        addAirport()
    