import socket
import threading
import random
import socket

# Se crea el socket del cliente
from db_interaction import set_default_schema, user_exists, get_user_by_username_and_password, insert_user

# Función para manejar la recepción de mensajes del servidor
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Error al recibir mensajes del servidor.")
            break

# Función para crear un usuario
def create_user(username):
    # se establece el esquema por defecto
    set_default_schema()
    while True:
        password = input("Ingresa tu contraseña: ")
        if len(password) > 16:
            print("La contraseña debe tener como máximo 16 caracteres. Inténtalo de nuevo.")
            continue
        if not password:
            print("La contraseña no puede estar vacía. Inténtalo de nuevo.")
            continue
        full_name = input("Ingresa tu nombre completo: ")
        if not full_name:
            print("El nombre completo no puede estar vacío. Inténtalo de nuevo.")
            continue
        insert_user(username, password, full_name)
        break

# Función para validar la dirección IP del servidor
def validate_server_address(server_address):
    if not server_address:
        server_address = "127.0.0.1"
    try:
        socket.inet_aton(server_address)
    except socket.error:
        print("La dirección IP ingresada no es válida. Inténtalo de nuevo.")
        return False
    return True

# Función para validar el puerto del servidor
def validate_server_port(server_port):
    try:
        server_port = int(server_port)
        if 1 <= server_port <= 65535:
            # check if the port is available
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                return s.connect_ex(('localhost', server_port)) != 0
        else:
            raise ValueError
    except ValueError:
        print("El puerto debe ser un número entero entre 1 y 65535. Inténtalo de nuevo.")
        return False

# verificar si el usuario existe
def verify_user():
    while True:
        username = input("Ingresa tu nombre de usuario: ")
        if not username:
            print("El nombre de usuario no puede estar vacío. Inténtalo de nuevo.")
            continue
        if not user_exists(username):
            # si el usuario no existe, se pregunta si desea crearlo
            create_new_user = input("El usuario no existe. ¿Deseas crearlo? (s/n): ")
            if create_new_user.lower() == "s":
                create_user(username)
                continue
            else:
                print("Finalizando sesion...")
                return
        else:
            break
    return username

# Ingresar servidor y puerto
def get_server_address():
    while True:
        server_address = input("Ingresa la dirección IP del servidor: ")
        if validate_server_address(server_address):
            break

    while True:
        server_port_input = input("Ingresa el puerto del servidor: ")
        if not server_port_input:
            server_port = random.randint(1, 65535)
            break
        if validate_server_port(server_port_input):
            server_port = int(server_port_input)
            break
    return server_address, server_port

# Función para autenticar al usuario
def authenticate_user(username):
    while True:
        password = input("Ingresa tu contraseña:")
        if not password:
            print("La contraseña no puede estar vacía. Inténtalo de nuevo.")
            continue
        if not get_user_by_username_and_password(username, password):
            print("La contraseña es incorrecta. Inténtalo de nuevo.")
            continue
        else:
            break

# Función principal
def main():
    # se verifica si el usuario existe
    username = verify_user()
    if username:
        # se autentica al usuario
        authenticate_user(username)
        # se obtiene la dirección IP y el puerto del servidor
        server_address, server_port = get_server_address()
        # se inicia el chat
    else:
        print("No se pudo iniciar el chat.")

    try:
        # Crear el socket del cliente
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_address, server_port))
        print(f"Conectado al servidor '{server_address}'.")
        
        # Enviar el nombre de usuario al servidor
        client.send(username.encode('utf-8'))
        
        # Iniciar el hilo para recibir mensajes del servidor
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.start()
        
        while True:
            # Leer el mensaje a enviar
            message = input()

            # Enviar el mensaje al servidor
            client.send(message.encode('utf-8'))
            
            # Salir si se envía "chao"
            if message.lower() == "chao":
                break
    except:
        print("No se pudo conectar al servidor.")
    
    client.close()

if __name__ == "__main__":
    main()