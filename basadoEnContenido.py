import numpy as np
import pandas as pd
import math

def crear_lista_etiquetas(movies):
    return sorted(set(etiqueta for lista in movies["genres"] for etiqueta in lista))

def calculoMatrizTF(peliculas, listaEtiquetas):
    TF = np.zeros((len(peliculas), len(listaEtiquetas)))
    etiqueta_idx = {etiqueta: j for j, etiqueta in enumerate(listaEtiquetas)}
    for i, (_, pelicula) in enumerate(peliculas.iterrows()):
        for etiqueta in pelicula["genres"]:
            j = etiqueta_idx[etiqueta]
            TF[i, j] += 1
    return TF

def calculoIDF(listaEtiquetas, peliculas):
    IDF = np.zeros(len(listaEtiquetas))
    todos_los_productos = len(peliculas)
    for j, etiqueta in enumerate(listaEtiquetas):
        contador = sum(1 for _, pelicula in peliculas.iterrows() if etiqueta in pelicula["genres"])
        IDF[j] = math.log10(todos_los_productos / (contador if contador > 0 else 1))
    return IDF

def calculoMatrizTFIDF(TF, IDF):
    return TF * IDF

def normalizarMatrizTFIDF(TFIDF):
    norma = np.linalg.norm(TFIDF, axis=1, keepdims=True)
    norma[norma == 0] = 1  # Evitar división por cero
    return TFIDF / norma


def calculoW(ratings, num_usuarios, num_items_real, item2idx):
    W = np.zeros((num_usuarios, num_items_real))
    medias = ratings.groupby("user")["label"].mean().to_dict()
    for _, fila in ratings.iterrows():
        user_idx = fila["user"] - 1
        item_idx = item2idx[fila["item"]]
        W[user_idx, item_idx] = fila["label"] - medias[fila["user"]]
    return W

def calculoPerfilesUsuario(W, TFIDF_normalizado):
    # TFIDF_normalizado: num_items x num_features
    # W: num_usuarios x num_items
    
    return W @ TFIDF_normalizado  # resultado: num_usuarios x num_features

def calculoDistanciaCoseno(usuario_vector, producto_vector):
    numerador = np.dot(usuario_vector, producto_vector)
    norma_usuario = np.linalg.norm(usuario_vector)
    norma_producto = np.linalg.norm(producto_vector)
    if norma_usuario == 0 or norma_producto == 0:
        return 0.0
    return numerador / (norma_usuario * norma_producto)

def obtenerRecomendaciones(lista_id_buscar, num_recomendaciones, W, perfil_usuario, TFIDF_normalizado, idx2item):
    recomendaciones = {}
    for id_usuario in lista_id_buscar:
        usuario_idx = id_usuario - 1
        usuario_vector = perfil_usuario[usuario_idx, :]
        sims = np.array([calculoDistanciaCoseno(usuario_vector, TFIDF_normalizado[i, :])
                         if W[usuario_idx, i] == 0 else -1
                         for i in range(TFIDF_normalizado.shape[0])])
        top_idx = np.argsort(sims)[-num_recomendaciones:][::-1]
        recomendaciones[id_usuario] = [idx2item[i] for i in top_idx]
    return recomendaciones



def basado_en_contenido(user):
    ratings = pd.read_csv("ml-1m/ratings.dat", sep="::",
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

    lista_etiqueta = crear_lista_etiquetas(movies)
    TF = calculoMatrizTF(movies, lista_etiqueta)
    IDF = calculoIDF(lista_etiqueta, movies)
    TFIDF = calculoMatrizTFIDF(TF, IDF)
    TFIDF_normalizado = normalizarMatrizTFIDF(TFIDF)


    # Mapear IDs de películas a índices consecutivos
    item2idx = {item_id: i for i, item_id in enumerate(sorted(movies["item"]))}
    idx2item = {i: item_id for item_id, i in item2idx.items()}
    num_items_real = len(item2idx)
    num_usuarios = ratings["user"].max()

    W = calculoW(ratings, num_usuarios, num_items_real, item2idx)
    perfil_usuario = calculoPerfilesUsuario(W, TFIDF_normalizado)

    lista_id_buscar = [user]
    num_recomendaciones = 10
    recomendaciones = obtenerRecomendaciones(lista_id_buscar, num_recomendaciones, W, perfil_usuario, TFIDF_normalizado, idx2item)
    return recomendaciones