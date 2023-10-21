users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dict = {"Общее количество": 0, "Уникальные посещения": 0}

amount = len(users)
uamount = set(users)
auamount = len(uamount)

dict["Общее количество"] = amount
dict["Уникальные посещения"] = auamount
print (dict)