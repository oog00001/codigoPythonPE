import numpy as np
import pandas as pd
import math

def crear_lista_etiquetas(movies):
    return sorted(set(etiqueta for lista in movies["genres"] for etiqueta in lista))

# Calculamos la matriz TF, se calculara como un diccionario dode la clave sera (id_pelicula, etiqueta)
# Recorreremos las peliculas y contaremos cuantas veces una etiqueta se encuentra dentro del mismo
def calculoMatrizTF(peliculas, listaEtiquetas):
  TF = {}
  for _, pelicula in peliculas.iterrows():
    for etiqueta in listaEtiquetas:
      cuenta = pelicula["genres"].count(etiqueta)
      TF[(pelicula["item"], etiqueta)] = cuenta
  return TF


def calculoIDF(listaEtiquetas, peliculas):
  IDF = {}
  todos_los_productos = len(peliculas)
  for etiqueta in listaEtiquetas:
    contador = 0
    for _, pelicula in peliculas.iterrows():
      if etiqueta in pelicula["genres"]:
        contador += 1
    IDF[etiqueta] = math.log10(todos_los_productos / contador)
  return IDF

# Calcularemos la matriz TF-IDF, aunque sera construida como un diccionario.
# Usaremos el diccionario TF con clave id_pelicula/etiqueta
# Usaremos el diccionario IDF con clave etiqueta
# El resultado es un diccionario TFIDF con clave id_pelicula/etiqueta

def calculoMatrizTFIDF(TF, IDF):
  TFIDF = {}
  for clave, valor in TF.items():
    TFIDF[clave] = valor * IDF[clave[1]]
  return TFIDF

# Normalizaremos el diccionario TFIDF
# Realizaremos una normalizacion por filas, es decir, que lo realizaremos teniendo en cuenta el id_producto, es decir la clave[0] de TFIDF
# El resultado es un diccionario TFIDF_normalizado con clave id_pelicula/etiqueta

def normalizarMatrizTFIDF(peliculas, TFIDF):
  TFIDF_normalizado = {}
  for _, pelicula in peliculas.iterrows():
    denominador = math.sqrt(sum(valor**2 for clave, valor in TFIDF.items() if clave[0] == pelicula["item"]))
    etiquetas_pelicula = pelicula["genres"]
    for etiqueta in etiquetas_pelicula:
      TFIDF_normalizado[(pelicula["item"], etiqueta)] = TFIDF[(pelicula["item"], etiqueta)] / denominador
  return TFIDF_normalizado

# Para poder realizar el perfil de usuario es necesario calcular una variable W. Este valor sera la diferencia entre el rating real del usuario menos el promedio de rating del usuario
# Primero deberemos conocer todos los rating que ha dado el usuario y la suma de los mismos, recorremos el diccionario de rating sacando estos dos datos para cada usuario
# Acto seguido calcularemos la media de rating de cada usuario a partir de lo calculado previamente.
# Finalmente calcularemos W, como un diccionario, para cada (usuario, producto) el resultado sera el rating del producto, menos la media del usuario

def calculoW(ratings):
  w = {}
  medias = {}
  suma_ratings_usuario = {}
  numero_raitings_usuario = {}
  for _, fila in ratings.iterrows():
    user = fila["user"]
    label = fila["label"]
    if user not in suma_ratings_usuario:
        suma_ratings_usuario[user] = label
        numero_raitings_usuario[user] = 1
    else:
        suma_ratings_usuario[user] += label
        numero_raitings_usuario[user] += 1

  for user, suma in suma_ratings_usuario.items():
        medias[user] = suma / numero_raitings_usuario[user]

  for _, fila in ratings.iterrows():
        user = fila["user"]
        item = fila["item"]
        label = fila["label"]
        w[(user, item)] = label - medias[user]

  return w



def mainDelColaborativo():
    rating = pd.read_csv("ml-1m/ratings.dat", sep="::",
                   names=["user", "item", "label", "timestamp"],
                   engine="python")
    
    movies = pd.read_csv( "ml-1m/movies.dat", sep="::",
        names=["item", "title", "genres"],
        engine='python',
        encoding="latin-1"
    )
    movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))

    users = pd.read_csv( "ml-1m/users.dat", sep="::",
        names=["user", "age", "sex", "occupation", "zipcode"],
        engine='python',
        encoding="latin-1"
    )
    
    # Creamos lista de etiquetas
    lista_etiqueta = crear_lista_etiquetas(movies)
    print(lista_etiqueta)

    # Creamos el TF
    TF = calculoMatrizTF(movies, lista_etiqueta)

    # Creamos el IDF
    IDF = calculoIDF(lista_etiqueta, movies)

    # Calcular matriz TFIDF
    TFIDF = calculoMatrizTFIDF(TF, IDF)

    # Normalizar la matriz
    TFIDF_normalizado = normalizarMatrizTFIDF(movies, TFIDF)

    # Perfil de usuario
    w = calculoW(rating)






mainDelColaborativo()
