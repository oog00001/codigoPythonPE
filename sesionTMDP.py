import requests

API_KEY = "TU_API_KEY"

# Paso 1: Obtener token
def obtener_token():
    url = f"https://api.themoviedb.org/3/authentication/token/new?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data.get("success"):
        return data["request_token"]
    else:
        raise Exception("No se pudo obtener el token: " + str(data))

# Paso 2: Autorizar token con usuario y contraseña
def autorizar_token(token, username, password):
    url = f"https://api.themoviedb.org/3/authentication/token/validate_with_login?api_key={API_KEY}"
    payload = {
        "username": username,
        "password": password,
        "request_token": token
    }
    response = requests.post(url, data=payload)
    data = response.json()
    if data.get("success"):
        return True
    else:
        raise Exception("Autenticación fallida: " + str(data))

# Paso 3: Crear sesión
def crear_sesion(token):
    url = f"https://api.themoviedb.org/3/authentication/session/new?api_key={API_KEY}"
    payload = {"request_token": token}
    response = requests.post(url, data=payload)
    data = response.json()
    if data.get("success"):
        return data["session_id"]
    else:
        raise Exception("No se pudo crear la sesión: " + str(data))

# Paso 4: Cerrar sesión
def cerrar_sesion(session_id):
    url = f"https://api.themoviedb.org/3/authentication/session?api_key={API_KEY}"
    payload = {"session_id": session_id}
    response = requests.delete(url, data=payload)
    data = response.json()
    if data.get("success"):
        print("Sesión cerrada correctamente.")
    else:
        print("Error al cerrar sesión:", data)



# --- Programa principal ---
def crear_sesion(username, password):
    
    try:
        token = obtener_token()
        print("Token obtenido:", token)

        autorizar_token(token, username, password)
        print("Usuario autenticado correctamente.")

        session_id = crear_sesion(token)
        print("Sesión creada con ID:", session_id)

        # Aquí puedes usar la sesión para consultar la API...

    except Exception as e:
        print("Error:", e)
    finally:
        # Cerrar sesión al finalizar
        if 'session_id' in locals():
            cerrar_sesion(session_id)
    