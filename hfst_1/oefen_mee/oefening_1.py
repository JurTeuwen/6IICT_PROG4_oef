def maak_persoonsinformatie_dict(naam, leeftijd, massa, lengte, oogkleur):
    """Geef een dictionary terug met alle gegevens die als parameters aan
    de functie meegegeven werden.
    
    >>> maak_persoonsinformatie_dict("Jan", 32, 79, 167, "blauw")
    {'naam': 'Jan', 'leeftijd': 32, 'massa': 79, 'lengte': 167, 'oogkleur': 'blauw'}
    """
    informatie = {}

    informatie["naam"] = naam
    informatie["leeftijd"] = leeftijd
    informatie["massa"] = massa
    informatie["lengte"] = lengte
    informatie["oogkleur"] = oogkleur
    return informatie


print(maak_persoonsinformatie_dict("Jan", 32, 79, 167, "blauw"))