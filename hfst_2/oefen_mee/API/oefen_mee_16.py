import json, requests 

antwoord = requests.get("https://api.covid19api.com/country/united-kingdom/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-03-07T00:00:00Z").text
antwoord_dict = json.loads(antwoord)
print(antwoord_dict)
