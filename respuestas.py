# codigos
# 0 - filtro colaborativo
# 1 - basado en contenidos
# 2 -
# 3 -

# mensaje 'codigo;nombreUsuario;-;-;'

import filtroColaborativo
import basadoEnContenido

def autentificacion():
    return 0

def obtener_los_nombres_peliculas_deIDs_colaborativo(recomendacion):
    return 0

def obtener_los_nombres_peliculas_deIDs_contenidos(recomendacion):
    return 0

def realizar_accion(mensaje):
    partes = mensaje.split(':')
    id_mensaje = partes[0]
    print(id_mensaje)
    nombre_usuario = partes[1]
    contrasena = partes[2]
    id_usuario = 1
    if(id_mensaje == '0'):
        recomendacion = filtroColaborativo.filtro_colaboratibo(id_usuario)
        respuesta = obtener_los_nombres_peliculas_deIDs_colaborativo(recomendacion)
    if(id_mensaje == '1'):
        respuesta = basadoEnContenido.basado_en_contenido(id_usuario)
        respuesta = obtener_los_nombres_peliculas_deIDs_contenidos(recomendacion)
    return respuesta
