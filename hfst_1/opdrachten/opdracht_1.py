dict = {3: 0, 5: 1, 10: 1, 8: 2, 15: 4}

""" Geef aan wat volgende code print"""
# Vul aan:{3: 0, 5: 1, 10: 1, 8: 2, 15: 4}
print(dict)

# Vul aan:3 5 10 8 15
for x in dict:
    print(x)

# Vul aan:3 5 10 8 15
for x in dict.keys():
    print(x)

# Vul aan:0 1 1 2 4
for x in dict.values():
    print(x)
