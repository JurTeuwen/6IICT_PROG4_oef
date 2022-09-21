films = [ "Monty Python and the Holy Grail",
          "Monty Python's Life of Brian",
          "Monty Python's Meaning of Life",
          "And Now For Something Completely Different"]

scores = [
    [ 9, 10, 9.5, 8.5, 3, 7.5 ,8 ], # Grail
    [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ], # Brian
    [ 7, 6, 5 ], # Life
    [ 6, 5, 6, 6 ] # Different
] 

dict = {}

for film in films:
    for score in scores:
        dict[film] = score
        scores.remove(score)
        break

print(dict)


for film,score in dict.items():
    som = sum(score)
    gemiddelde = round(som/len(score), 1)
    print(gemiddelde)    