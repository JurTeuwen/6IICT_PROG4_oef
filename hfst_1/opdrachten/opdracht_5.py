poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}

for naam in poll_talen:
    if naam in favorite_languages:
        print(f"{naam},bedankt voor het invullen")
    else:
        antwoord = input(f"{naam},wat is je favoriete taal: ")
        if antwoord == "":
            print("je hebt niks geantwoord,rens is een ezel")
        else:
            favorite_languages[naam]= antwoord
print(favorite_languages)