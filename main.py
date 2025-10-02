
import sys
import os
import recepcion
import cargarDatos

import cornac
from cornac.datasets import movielens
from cornac.data import Reader


def main():
    # para las pruebas pondremos diez intentos en la practica sera un while true
    numero_intentos = 10

    #data = movielens.load_feedback(fmt="UIR", variant="1M", reader=Reader())
    #print(data)

    # Esto unicamente devuelve una descripcion y esta completamente desactualizado
    #item_features = movielens.load_plot()

    #print(item_features)
    #peliculas,usuarios,rating, usuarios_real = cargarDatos.cargar_datos()
    # rating no tiene el mismo formato, no lo utilizaremos
    #print(rating)

    while(numero_intentos != 0):
        recepcion.recibir_peticion_frontend()
        numero_intentos = numero_intentos - 1





main()