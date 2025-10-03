import pandas as pd
import requests

# las peliculas son id,title,genre_ids,poster_path

def cargar_peliculas():
    movie = pd.read_csv(pruebasConAPI.movies_dir_o)
    return movie




def detallesUsuario(id_usuario):
    url = "https://api.themoviedb.org/3/person/{id_usuario}?language=en-US"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    print(response.text)
    return response

def listaPeliculasDeUsuario(id_usuario):
    url = "https://api.themoviedb.org/3/person/{id_usuario}/movie_credits?language=en-US"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    print(response.text)
    return response

def cargar_usuarios():
    data = pd.read_csv("ml-1m/ratings.dat", sep="::",
                    names=["user", "item", "label", "timestamp"])
    




def cargar_ratings():
    data = pd.read_csv("ml-1m/ratings.dat", sep="::",
                    names=["user", "item", "label", "timestamp"])