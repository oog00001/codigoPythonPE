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

def realizar_accion(mensaje):
    partes = mensaje.split(';')
    id_mensaje = partes[0]
    nombre_usuario = partes[1]
    contrasena = partes[2]
    if(id_mensaje == '0'):
        respuesta = filtroColaborativo.filtro_colaboratibo(nombre_usuario)
    if(id_mensaje == '1'):
        respuesta = basadoEnContenido.basado_en_contenido(nombre_usuario)
    return respuesta
