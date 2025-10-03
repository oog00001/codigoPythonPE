import pandas as pd
import requests
import ObtenerPelisAPI

# las peliculas son id,title,genre_ids,poster_path

def cargar_peliculas_tmdb():
    movie = pd.read_csv(ObtenerPelisAPI.movies_dir_o)
    return movie

def cargar_peliculas_movilens():
    movies = pd.read_csv( "ml-1m/movies.dat", sep="::",
        names=["item", "title", "genres"],
        engine='python',
        encoding="latin-1"
    )
    return movies




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
    return data