import requests

def getAirport():
    url = "https://airport-info.p.rapidapi.com/airport"

    querystring = {"iata":"vlc"}

    headers = {
        "X-RapidAPI-Key": "8c092e30bbmshb9c5188d47a36d5p1e91ccjsnd35144ec1afd",
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.jason()
        print(data[id])
        data["iata"]
        data["name"]
        data["location"]
        data["city"]
        data["country"]
        data["website"]
        data["phone"]


