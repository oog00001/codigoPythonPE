import numpy as np
import pandas as pd
from libreco.data import random_split, DatasetPure
from libreco.algorithms import LightGCN  # pure data, algorithm LightGCN
from libreco.algorithms import SVD
from libreco.evaluation import evaluate

import cargarDatos

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def filtro_colaboratibo(nombre_usuario):

    tf.reset_default_graph()   # <<< IMPORTANTE


    train_df = cargarDatos.cargar_ratings()
    test_df = cargarDatos.cargar_peliculas_tmdb()

    # split whole data into three folds for training, evaluating and testing
    train_data, data_info = DatasetPure.build_trainset(train_df)
    eval_data = DatasetPure.build_evalset(train_df)

    svd = SVD(
        task="rating",         # "rating" porque queremos predecir ratings
        data_info=data_info,
        embed_size=32,         
        n_epochs=3,            
        lr=0.005,              
        batch_size=2048        
    )
    # monitor metrics on eval data during training
    svd.fit(
        train_data,
        neg_sampling=False,
        verbose=2,
        eval_data=eval_data,
        metrics=["rmse", "mae"]
    )

    test_items = test_df['title'].tolist()
    #print(test_items)

    predicciones = []
    for item in test_items:
        score = svd.predict(user=nombre_usuario, item=item, cold_start="average")
        predicciones.append((item, score))

    # Ordenar por score descendente y quedarnos con top N
    predicciones = sorted(predicciones, key=lambda x: x[1], reverse=True)[:7]

    recomendacion = []
    movies = cargarDatos.cargar_peliculas_movilens()

    #### En la practica debe de cargarse desde tmbd

    for item_id, score in predicciones:
        for _, pelicula in movies.iterrows():
            if item_id == pelicula["item"]:
                recomendacion.append(pelicula["title"])
        print(item_id, score)

    print(predicciones)
    print(recomendacion)
    return recomendacion


filtro_colaboratibo(1)