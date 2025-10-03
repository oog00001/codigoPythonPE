import numpy as np
import pandas as pd
from libreco.data import random_split, DatasetPure
from libreco.algorithms import LightGCN  # pure data, algorithm LightGCN
from libreco.algorithms import SVD
from libreco.evaluation import evaluate

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def filtro_colaboratibo(nombre_usuario):

    tf.reset_default_graph()   # <<< IMPORTANTE


    data = pd.read_csv("ml-1m/ratings.dat", sep="::",
                    names=["user", "item", "label", "timestamp"])

    # split whole data into three folds for training, evaluating and testing
    train_data, eval_data, test_data = random_split(data, multi_ratios=[0.8, 0.1, 0.1])

    train_data, data_info = DatasetPure.build_trainset(train_data)
    eval_data = DatasetPure.build_evalset(eval_data)
    test_data = DatasetPure.build_testset(test_data)
    print(data_info)  

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

    recomendacion = svd.recommend_user(user=nombre_usuario, n_rec=7, cold_start="average")
    return recomendacion

