""" Niveau 1 """
puntenlijst = [
    ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], # 1 punt
    ["D", "G"],                                         # 2 punten
    ["B", "C", "M", "P"],                               # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    ["K"],                                              # 5 punten
    ["J", "X"],                                         # 6 punten
    ["Q","Z"]                                           # 7 punten
]

def punten_berekenen(puntenlijst):
    dict_puntenlijst = {}
    for index,value in enumerate(puntenlijst):
        for index1,value1 in enumerate(value):
            dict_puntenlijst[value1] = index+1
    dict_puntenlijst_2={}
    for i in sorted(dict_puntenlijst):
        dict_puntenlijst_2[i]=dict_puntenlijst[i]
    
    return dict_puntenlijst_2
            
# print(punten_berekenen(puntenlijst))

""" Niveau 2"""
puntenlijst_en = [
    ["A", "E", "I", "O", "U", "L", "N", "S", "T"],      # 1 punt
    ["D", "G", "K"],                                    # 2 punten
    ["B", "M", "P", "Q", "R"],                          # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    [],                                                 # 5 punten
    ["J", "X"],                                         # 6 punten
    ["C","Z"]                                           # 7 punten
]

def punten_berekenen(puntenlijst):
    dict_puntenlijst = {}
    for index,value in enumerate(puntenlijst):
        for index1,value1 in enumerate(value):
            dict_puntenlijst[value1] = index+1
    dict_puntenlijst_2={}
    for i in sorted(dict_puntenlijst):
        dict_puntenlijst_2[i]=dict_puntenlijst[i]
    
    return dict_puntenlijst_2
            
# print(punten_berekenen(puntenlijst_en))

def score_nederlands_dict(punten):
    totaal = 0
    dict_puntenlijst = punten_berekenen(punten)
    woord = input("geef een woord: ")

    for kar in woord:
        punt = dict_puntenlijst.get(kar)
        totaal = totaal+punt
    return totaal

# print(score_nederlands_dict(puntenlijst))

def score_engels_dict(punten):
    totaal = 0
    dict_puntenlijst = punten_berekenen(punten)
    woord = input("geef een woord: ")

    for kar in woord:
        punt = dict_puntenlijst.get(kar)
        totaal = totaal+punt
    return totaal

# print(score_engels_dict(puntenlijst_en))


def score_nederlands_list(punten):
    totaal = 0
    woord = input("geef een woord: ")
    for kar in woord:
        for index,lijst in enumerate(punten):
            if kar in lijst:
                punt = index+1
                totaal = totaal+punt
    return totaal

# print(score_nederlands_list(puntenlijst))


def score_engels_list(punten):
    totaal = 0
    woord = input("geef een woord: ")
    for kar in woord:
        for index,lijst in enumerate(punten):
            if kar in lijst:
                punt = index+1
                totaal = totaal+punt
    return totaal

# print(score_nederlands_list(puntenlijst_en))


print(score_nederlands_dict(puntenlijst))
print(score_nederlands_list(puntenlijst))
print(score_engels_dict(puntenlijst_en))
print(score_engels_list(puntenlijst_en))