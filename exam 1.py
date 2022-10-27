import requests, json
hotels = {}
def getHotelsByName(name):
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    hotel = "Hotel Recoletos Madrid"
    querystring = {"q":""+hotel+"","locale":"en_US","langid":"1033","siteid":"300000001"}

    headers = {
	"X-RapidAPI-Key": "8c092e30bbmshb9c5188d47a36d5p1e91ccjsnd35144ec1afd",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if (response.status_code == 200):
        jsonResult = response.json()
        hotelDic = {}
        for hotel in jsonResult["sr"]:
            hotelDic[hotel["hotelId"]] = {
                "Name": hotel["regionNames"]["shortNames"],
                "Adress": hotel["hoteladress"]["street"],
                "City": hotel["hoteladress"]["city"],
                "Province": hotel["hoteladress"]["province"]
            }
        return hotelDic
    return None

def getReviewsById(hotelId):
    url = "https://hotels4.p.rapidapi.com/reviews/v3/list"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotelId,
        "size": 10,
        "startingIndex": 0
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "8c092e30bbmshb9c5188d47a36d5p1e91ccjsnd35144ec1afd",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if (response.status_code == 200):
        jsonResult = response.json()
        reviews = []
        for review in jsonResult["data"]["propertyInfo"]["reviewInfo"]["reviews"]:
            if(len(review["text"])):

        return reviews

def getHotelDetailById(hotelId):
    url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotelId
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "8c092e30bbmshb9c5188d47a36d5p1e91ccjsnd35144ec1afd",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if (response.status_code == 200):
        jsonResult = response.json()
        return jsonResult["data"]["propertyReviewSummaries"][0]["overalScoreWithDescription"]
    return None

def getValue(hotelId):

    url = "https://hotels4.p.rapidapi.com/reviews/v3/get-summary"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotelId
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "8c092e30bbmshb9c5188d47a36d5p1e91ccjsnd35144ec1afd",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if (response.status_code == 200):
        jsonResult = response.json()
    return jsonResult["data"]["propertyInfo"][0]["propertyReviewCountDetails"]["reviewDisclainer"]

while(True):
    print("I have ", len(hotels), " favourites Hotels :)")
    print("1.- Search hotel bu Name")
    print("2.- Quality by Id")
    print("3.- Import hotel by Id")
    print("4.- List hotels")
    print("5.- List reviews by Id")
    print("6.- List hotels by value")
    print("7.- Exit")
    option = input("Select option: ")

    if(option == 7):
        print("BYE! Thanks for using the application ;)")
        break
    elif(option == 1):
        name = input("Enter name hotel: ")
        hotels = getHotelsByName(name)
        print("HOTEL Id INFO")
        print("\t", hotelId)

    elif(option == 2):
        idh = input("Enter hotel Id: ")
        print("Quality: ", getValue(idh))
    elif(option == 3):
        idh = input("Enter hotel Id: ")
        hotel = getHotelDetailById(idh)
        if hotel != None:
            print("Importing....")
            reviews = getReviewsById(idh)
            if reviews != None:
                hotel["reviews"] = reviews
                hotels["hotelId"] = hotel
                print("Imported successfully")
    elif(option == 4):
        print("Listing Hotels")
        for hotel.detail in hotels.items():
            print(hotel)
            print("\tName:", detail["name"])
    elif(option == 5):
        idh = input("Enter hotel Id: ")
        print(getValue(idh))
    elif(option == 6):
        q = float(input("Enter min quality [0-10]: "))
        print("Listing Hotels....")
        for hotel.detail in hotels.items():
            if(float(detail["value"].split("/")[0]) >= q):
                print(hotel)