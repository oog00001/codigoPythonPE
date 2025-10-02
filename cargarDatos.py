


def cargar_peliculas():
    peliculas = []

    with open("ml-1m/movies.dat", "r", encoding="latin-1") as f:
        for linea in f:
            linea = linea.strip()
            partes = linea.split("::")
            
            if len(partes) > 0:
                movie_id = partes[0]
                titulo = partes[1]
                generos = partes[2].split("|")

                peliculas.append({
                    "id": movie_id,
                    "titulo": titulo,
                    "generos": generos
                })

    return peliculas

def cargar_usuarios():
    usuarios = []

    with open("ml-1m/users.dat", "r", encoding="latin-1") as f:
        for linea in f:
            linea = linea.strip()
            partes = linea.split("::")

            if len(partes) > 0:
                user_id = partes[0]
                genero = partes[1]
                age = partes[2]
                occupation = partes[3]

                usuarios.append({
                    "id": user_id,
                    "genero": genero,
                    "age": age,
                    "occupation": occupation

                })

    return usuarios

def cargar_ratings():
    ratings = []

    with open("ml-1m/ratings.dat", "r", encoding="latin-1") as f:
        for linea in f:
            linea = linea.strip()
            partes = linea.split("::")

            if len(partes) > 0:
                user_id = partes[0]
                item_id = partes[1]
                rating = partes[2]

                ratings.append({
                    "id_user": user_id,
                    "id_item": item_id,
                    "rating": rating,

                })

    return ratings


def cargar_privado():
    usuarios_real = []

    with open("ml-1m/privados.dat", "r", encoding="latin-1") as f:
        for linea in f:
            linea = linea.strip()
            partes = linea.split("::")

            if len(partes) > 0:
                user_id = partes[0]
                nombre = partes[1]
                contrasena = partes[2]

                usuarios_real.append({
                    "id": user_id,
                    "nombre": nombre,
                    "contrasena": contrasena

                })

    return usuarios_real

def cargar_datos():
    peliculas = cargar_peliculas()
    usuarios = cargar_usuarios()
    rating = cargar_ratings()
    usuarios_real = cargar_privado()
    return peliculas,usuarios,rating, usuarios_real