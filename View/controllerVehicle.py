from vehicle import Vehicle

class ControllerVehicle:
    def __init__(self):
        self.__vehicles = {}   #key->Plate/Value->Vehicle

    def addVehicle(self, plate, desc, chasis, driver):
        if plate in self.__vehicles:
            return False
        else:
            newVehicles = Vehicle(plate, chasis, driver)
            self.__vehicles[plate] = newVehicles
            return True

    def deleteVehicle(self, plate):
        if plate not in self.__vehicles:
            return False
        else:
            return self.__vehicles.pop(plate) #del self.__vehicles[plate]

    def getNumberOfVehicles(self):
        return len(self.__vehicles)

    def addOdometer(self, plate, date, fromCity, toCity, kms):
        if plate not in self.__vehicles:
            return False
        else:
            vehicle = self.__vehicles[plate]
            vehicle.addOdometer(date, fromCity, toCity, kms)
            return True

    def getVehicles(self):
        return self.__vehicles

    def confirmOdometer(self, plate, date):
        if plate not in self.__vehicles:
            return False
        vehicle = self.__vehicles[plate]
        if date not in vehicle.getOdometer():
            return False
        vehicle.confirmOdometer(date)
        return True