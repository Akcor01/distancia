usuarios = [{'user': 'userA', 'Following': ['userB', 'userD', 'userE', 'userG']},
            {'user': 'userB', 'Following': ['userC', 'userJ', 'userI', 'userE']},
            {'user': 'userC', 'Following': ['userM', 'userN', 'userJ', 'userI', 'userE']}]


def calc_distancia(dictionary):
    users, usuario1, usuario2, distancia = dictionary.values()
    visitados = set()

    # distancia = 0

    def get_dict(valor):
        for rec in usuarios:
            if valor in rec.values():
                return rec
            else:
                return False

    def _distancia(seguidores):
        for user_following in seguidores:
            if user_following == usuario2
                return distancia
            else:
                if get_dict(user_following):
                    diccionario = get_dict(user_following)
                    distancia += 1
                    calc_distancia({'users': diccionario, 'user1': 'userA', 'user2': 'userM', 'distancia': distancia})
                else:
                    distancia = 0
        return distancia

    if users['user'] != usuario1:
        if users['user'] == usuario2:
            return distancia
        if users['user'] not in visitadoos:
            visitados.add(users['user'])
            _distancia(users['Following'])
    else:
        _distancia(users['Following'])

    return -1  # No se encontró un camino entre los usuarios


usuario1 = 'userA'
usuario2 = 'userM'
for users in usuarios:
    distancia = _distancia({'users': users, 'user1': 'userA', 'user2': 'userM', 'distancia': 0})
if distancia != -1:
    print(f"La distancia entre {usuario1} y {usuario2}, es: {distancia}.")
else:
    print(f"No hay un camino de conexión entre {usuario1} y {usuario2}.")
