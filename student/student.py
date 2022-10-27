class Student:
    def __init__(self, dni, name, surnames, age, city, province, email):
        
        self.__dni = dni
        self.__name = name
        self.__surnames = surnames
        self.__age = age
        self.__city = city
        self.__province = province
        self.__email = email

    def getDni(self):
        return self.__dni

    def getName(self):
        return self.__name

    def getSurnames(self):
        return self.__surnames

    def getAge(self):
        return self.__age

    def getCity(self):
        return self.__city

    def getProvince(self):
        return self.__province

    def getEmail(self):
        return self.__email
    
