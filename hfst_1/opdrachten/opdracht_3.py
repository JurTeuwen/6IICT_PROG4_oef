""" Niveau 1"""
dict_1={1: 10, 2: 20}
dict_2={3: 30, 4: 40}
dict_3={5: 50, 6: 60}
# Resultaat: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# niveau_1_dict = {}
# for key,value in dict_1.items():
#     niveau_1_dict[key]=value
# for key,value in dict_2.items():
#     niveau_1_dict[key]=value
# for key,value in dict_3.items():
#     niveau_1_dict[key]=value
# print(niveau_1_dict)

""" Niveau 2 """
dict = {'a': 'Red', 'b': 'Green', 'c': None}
# Resultaat: {'a': 'Red', 'b': 'Green'}

# niveau_2_dict = {}
# for key,value in dict.items():
#     if value != None:
#         niveau_2_dict[key]=value
# # print(niveau_2_dict)

""" Niveau 3 """
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
# Resultaat: {'a': 400, 'b': 400, 'd': 400, 'c': 300})

# niveau_3_dict = {}
# for key1, value1 in dict_1.items():
#     for key2, value2 in dict_2.items():
#         if key1 == key2:
#             niveau_3_dict[key1]=value1+value2
#         else:
#            niveau_3_dict[key1]=value1
#            niveau_3_dict[key2]=value2
# print(niveau_3_dict)