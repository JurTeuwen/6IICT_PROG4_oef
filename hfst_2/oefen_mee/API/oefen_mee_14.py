import requests

antwoord = requests.get("https://api.covid19api.com/world/total").text #haal tekst van website en stophet in antwoord
print(antwoord) #print antwoord
