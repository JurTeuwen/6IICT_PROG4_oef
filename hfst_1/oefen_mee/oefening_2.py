boodschappen_lijst = ["appel","doerian","banaan","doerian","appel","kers",
"kers","mango","appel","appel","kers","doerian","banaan",
"appel","appel","appel","appel","banaan","appel"]

"""
Oplossing:
boodschappen_dict = {'appel': 9, 'doerian': 3, 'banaan': 3, 'kers': 3, 'mango': 1}

"""
boodschappen_dict = {}

for fruit in boodschappen_lijst:
    if fruit not in boodschappen_dict:
        x = boodschappen_lijst.count(fruit)
        boodschappen_dict[fruit] = x

print(boodschappen_dict)