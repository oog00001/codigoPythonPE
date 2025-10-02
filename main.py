
import sys
import os
import recepcion
import cargarDatos


def main():
    numero_intentos = 2
    while(numero_intentos != 0):
        recepcion.recibir_peticion_frontend()
        numero_intentos = numero_intentos - 1

main()