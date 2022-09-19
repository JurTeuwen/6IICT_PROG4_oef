engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

zin = input("Geef een zin in het engels: ")
nederlands_zin_lijst = []
zin_in_lijst = zin.split()
for woord in zin_in_lijst:
    nederlands_woord = engels_nederlands[woord]
    nederlands_zin_lijst.append(nederlands_woord)

nederlands_zin = " ".join(nederlands_zin_lijst)
print(nederlands_zin)