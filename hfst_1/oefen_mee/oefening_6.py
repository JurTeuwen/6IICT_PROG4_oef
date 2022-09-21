engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }


# # creating a new dictionary
# my_dict ={"Java":100, "Python":112, "C":11}

# # one-liner
# print("One line Code Key value: ", list(my_dict.keys())
# 	[list(my_dict.values()).index(100)])

vertaal = []
key_value_lijst = list(engels_nederlands.items())
print(key_value_lijst)
zin = input().split()

for woord in zin:
    for key,value in key_value_lijst:
        if woord == value:
            vertaal.append(key)
    vertaal.append(woord)

vertaalde_zin = " ".join(vertaal)
print(vertaalde_zin)