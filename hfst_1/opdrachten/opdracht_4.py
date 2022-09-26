""" Niveau 1 """
dict = {
    "belgie": {
        "provincie": {
            "naam": "limburg",
            "weetjes": {
                "oppervlakte":  2.422,
                "inwoners": 885.951,
                "gouverneur": "Jos Lantmeeters"
            }
        }
    }
}

# print(dict["belgie"]["provincie"]["weetjes"]["gouverneur"])

""" Niveau 2 """
dict["belgie"]["provincie"]["informatie"] = dict["belgie"]["provincie"].pop("weetjes")
# print(dict)

extra_info = [  ["mannen", 49.77], 
                ["vrouwen", 50.23], 
                ["hoofdstad", "hasselt"] ]

for key,value in enumerate(extra_info):
    dict["belgie"]["provincie"]["informatie"][value[0]] = value[-1]

print(dict)