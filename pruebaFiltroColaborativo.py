import numpy as np
import pandas as pd
from libreco.data import random_split, DatasetPure
from libreco.algorithms import LightGCN  # pure data, algorithm LightGCN
from libreco.algorithms import SVD
from libreco.evaluation import evaluate

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


# do final evaluation on test data
#evaluate(
#    model=lightgcn,
#    data=test_data,
#    neg_sampling=True,
#    metrics=["loss", "roc_auc", "precision", "recall", "ndcg"],
#)
 
user_id = 6040
item = 110
lista_item_recomendacion = []

rec_items = svd.recommend_user(user=user_id, n_rec=7, cold_start="average")
# Cold-start para usuario o item desconocido, se ignora si ya se conoce el elemento
pred_cold = svd.recommend_user(user="nuevo_usuario_123", n_rec=7, cold_start="average")
print(f"Recomendaciones para el usuario {user_id}:", rec_items)
print(f"Recomendaciones para el usuario {user_id}:", pred_cold)


# predict preference of user 2211 to item 110
#lightgcn.predict(user=user_internal, item=item_internal)
# recommend 7 items for user 2211
#lightgcn.recommend_user(user=user_internal, n_rec=7)

# cold-start prediction
#lightgcn.predict(user="ccc", item="not item", cold_start="average")
# cold-start recommendation
#lightgcn.recommend_user(user="are we good?", n_rec=7, cold_start="popular")

