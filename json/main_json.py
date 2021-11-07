import json

users_json = open('users.json', 'r')
users = json.load(users_json)
print(users)


#eliminar elemento
#user = list(filter(lambda x: x['id'] != 2, users))
#print(user)

#aumentar o quitar balance
user_id = 2
price = 0.2
for u in users:
    if u['id'] == user_id:
        u['balance'] += price
print(users)

#encontrar un usuario
#id = 3
#user = list(filter(lambda x: x['id'] == id, users))
#print(user)


# Reescribiendo json
#users_file = open('users.json', 'w')
#users_file.write(json.dumps(users))


if __name__ == '__main__':
    pass