fruitmand = { "appel":3, "banaan":5, "kers":50 }
print( fruitmand.keys() )
# Vul in --> return .keys(): dict_keys(['appel', 'banaan', 'kers'])
print( fruitmand.values() )
# Vul in --> return .values():dict_values([3, 5, 50])
print( fruitmand.items() )
# Vul in --> return .items(): dict_items([('appel', 3), ('banaan', 5), ('kers', 50)])
"""
Wat zijn de gelijkenissen van deze waarden met lijsten? Wat zijn de verschillen?
Hebben beiden vierkante haakjes
"""

"""
Zijn deze waarden effectief lijsten? Hoe kan je dit testen?
nee, door een functie uit te testen die alleen op lijsten werken
"""

"""
Indien nee, is het mogelijk om deze waarden naar lijsten om te vormen?
Via de typecasting functie list()
"""