import json

def registrar(update):
    pass


def usuario_existe(update):
    users_json = open('json/users.json', 'r')
    users = json.load(users_json)
    #print(users)
    # encontrar un usuario
    user_id = update.message.chat.id
    coinsidencias = list(filter(lambda x: x['id'] == user_id, users))
    if len(coinsidencias) > 0:
        return True
    else:
        return False