import cornac
from cornac.datasets import movielens
from cornac.data import Reader
from cornac.models import ItemKNN
from cornac.eval_methods import RatioSplit


def filtro_colaboratibo(nombre_usuario):
     # Cargo MovieLens 1M
    data = movielens.load_feedback(fmt="UIR", variant="1M", reader=Reader())

    #Así se divide los conjuntos usando cornac. 
    ratio_split = RatioSplit(
        data=data,
        test_size=0.2,
        rating_threshold=4.0,
        seed=123,
        exclude_unknowns=True,
        verbose=True
    )

    train_set = ratio_split.train_set

    #Utilizo como modelon KNN iten-user con la similaridad del coseno
    model = ItemKNN(k=30, similarity="cosine", name="ItemKNN")

    # Entreno
    model.fit(train_set)

    # Ahora cojo un usuario aleatorio
    user_id = random.choice(train_set.user_ids)
    print("Usuario seleccionado:", user_id)
    #Aquí mapeo el usuario seleccionado del dataset con el que usa cornac
    user_idx = train_set.uid_map[user_id]

    # Obtengo el ranking completo para ese usuario
    ranked_items = model.rank(user_idx=user_idx)

    # Quito de la lista los items que ya ha visto el usuario
    seen_items = set(t[0] for t in train_set.user_data[user_idx])
    filtered_items = [(t[0], t[1]) for t in ranked_items if t[0] not in seen_items]

    #Ahora me quedo solo con el top 10

    top10 = []
    for t in ranked_items:
        item_idx = int(t[0])
        if item_idx not in seen_items:
            score = model.score(user_idx, item_idx)
            top10.append((item_idx, score))
    top10 = top10[:10]

    print(f"\nTop-10 recomendaciones para el usuario {user_id} (ItemKNN):")
    for item_idx, score in top10:
        item_idx = int(item_idx)  # convertir a entero
        item_id = train_set.item_ids[item_idx]  # Vuelvo a cambiar el id al del conjunto. 
        print(f"Item {item_id}, score={score:.4f}")

