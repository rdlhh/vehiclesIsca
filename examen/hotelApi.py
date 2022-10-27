import requests,json


def getHotelByName(name):

    result = {}

    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {"q":name}

    headers = {
        "X-RapidAPI-Key": "108c7f5582mshc21d14a4f92b988p1f31edjsnbdbe21df7051",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"    
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    hotelsJson = dict(json.loads(response.text))

    for hotel in range(len(hotelsJson["sr"])):
        id = hotelsJson["sr"][hotel]["hotelId"]
        result[id] = []
        result[id].append(hotelsJson["sr"][hotel]["regionNames"]["shortName"])
        result[id].append(hotelsJson["sr"][hotel]["hotelAddress"]["street"])
        result[id].append(hotelsJson["sr"][hotel]["hotelAddress"]["city"])
        result[id].append(hotelsJson["sr"][hotel]["hotelAddress"]["province"])
    return result

def getReviewsById(hotelId):

    reviews = []

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
        "X-RapidAPI-Key": "108c7f5582mshc21d14a4f92b988p1f31edjsnbdbe21df7051",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    reviewJson = dict(json.loads(response.text))

    for review in range(len(reviewJson["data"]["propertyInfo"]["reviewInfo"]["reviews"])):
        reviews.append(reviewJson["data"]["propertyInfo"]["reviewInfo"]["reviews"][review]["text"])
    return reviews

def getHotelDetailById(hotelId):

    detailId = {}

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
        "X-RapidAPI-Key": "108c7f5582mshc21d14a4f92b988p1f31edjsnbdbe21df7051",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    detailJson = dict(json.loads(response.text))

    detailId["name"] = detailJson["data"]["propertyInfo"]["summary"]["name"]

    detailId["address"] = detailJson["data"]["propertyInfo"]["summary"]["location"]["address"]["firstAddressLine"]

    detailId["city"] = detailJson["data"]["propertyInfo"]["summary"]["location"]["address"]["city"]

    detailId["province"] = detailJson["data"]["propertyInfo"]["summary"]["location"]["address"]["province"]

    detailId["value"] = detailJson["data"]["propertyInfo"]["reviewInfo"]["summary"]["overallScoreWithDescriptionA11y"]["value"]
    
    return detailId

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
        "X-RapidAPI-Key": "108c7f5582mshc21d14a4f92b988p1f31edjsnbdbe21df7051",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    valueJson = dict(json.loads(response.text))

    return valueJson["data"]["propertyReviewSummaries"][0]["overallScoreWithDescriptionA11y"]["value"]