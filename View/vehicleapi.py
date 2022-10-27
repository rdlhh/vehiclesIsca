import requests

def getDistance(source, dest):
    url = "https://distanceto.p.rapidapi.com/get"

    source = "Enguera"
    dest = "Alberic"
    querystring = {"route":"[{\"t\":\""+source+"\",\"c\":\"ES\"},{\"t\":\""+dest+"\",\"c\":\"ES\"}]","car":"true"}

    headers = {
        'x-rapidapi-host': "distanceto.p.rapidapi.com",
        'x-rapidapi-key': "498beeb34fmsh7558841455add94p17d283jsn987de2c3f201"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        meters = float(data["steps"][0]["distance"]["car"]["distance"])
        return meters