
import socket
import respuestas

def recibir_peticion_frontend():

    HOST = '127.0.0.1'  
    PORT = 5000 


    mensaje = '1:oog:00001'
    respuesta = respuestas.realizar_accion(mensaje)

    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #    s.bind((HOST, PORT))
    #    s.listen()
    #    print("Esperando conexión...")
    #    conn, addr = s.accept()
    #    with conn:
    #        print(f"Conectado con {addr}")
    #        while True:
    #            data = conn.recv(1024)
    #            if not data:
    #                break
                
    #            mensaje = data.decode()
    #            print("Mensaje recibido:", mensaje)

    #            #mensaje = '0;angel;contrasena'
    #            respuesta = respuestas.realizar_accion(mensaje)

    #            conn.sendall(respuesta.encode())