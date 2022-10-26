import json, requests 

antwoord = requests.get("https://api.covid19api.com/world/total").text
antwoord_dict = json.loads(antwoord)
print(antwoord_dict)
