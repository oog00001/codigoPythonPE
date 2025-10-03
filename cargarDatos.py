import pandas as pd
import pruebasConAPI
from typing import List

# las peliculas son id,title,genre_ids,poster_path

def cargar_peliculas():
    movie = pd.read_csv(pruebasConAPI.movies_dir_o)
    return movie

def cargar_usuarios():
    data = pd.read_csv("ml-1m/ratings.dat", sep="::",
                    names=["user", "item", "label", "timestamp"])
    movie = cargar_peliculas()
    moviesRated: List[pruebasConAPI.MovieOnDB]
    userProfile = pruebasConAPI.getUserProfile(moviesRated)
    print(userProfile)

def cargar_ratings():
    data = pd.read_csv("ml-1m/ratings.dat", sep="::",
                    names=["user", "item", "label", "timestamp"])