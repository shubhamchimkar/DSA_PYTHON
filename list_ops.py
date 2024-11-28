list_of_players=["virat","rohit","ravendra"]
print(list_of_players)#slicing
"""
two way of itterating list
"""
for player in list_of_players:
    print(player)

for i in range(0,len(list_of_players)):
    print(list_of_players[i])
list_of_num=[1,2,5,66,4]
list_of_new_num=[1,5,6,8]
l = list_of_num.extend(list_of_new_num)
print(dir(list_of_new_num))#dir used for posiible operation can be performed 