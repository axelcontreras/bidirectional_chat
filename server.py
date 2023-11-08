import socket
import threading
import db_interaction as db

clientes = {}
direcciones = {}
nombres_sockets = {}

def detener_servidor():
    print("Cerrando conexiones...")
    for cliente in clientes:
        cliente.close()
    server.close()

# Enviar mensajes a todos los clientes conectados

def broadcast(mensaje):
    for socket_cliente in clientes:
        socket_cliente.send(f"\n@server: {mensaje}".encode('utf-8'))

# Listar usuarios conectados

def enviar_lista_usuarios(socket_destino):
    lista_usuarios = "Lista de usuarios conectados:\n"
    for usuario in clientes.values():
        lista_usuarios += usuario + "\n"
    socket_destino.send(lista_usuarios.encode('utf-8'))

# Enviar mensaje a destino y guardar en la base de datos

def obtener_id_usuario(usuario):
    try:
        id_usuario = db.get_user_by_id(usuario)
        return id_usuario
    except Exception as e:
        raise(f"Error al obtener el ID del usuario: {e}")

def guardar_datos_mensaje(usuario_origen, usuario_destino, mensaje):
    try:
        id_user_origen = obtener_id_usuario(usuario_origen)
        id_user_destino = obtener_id_usuario(usuario_destino)
        db.insert_message(id_user_origen, id_user_destino, mensaje)
    except Exception as e:
        print(f"Error al guardar el mensaje en la base de datos: {e}")

def enviar_mensaje(socket_destino, mensaje):
    socket_destino.send(f"\n{mensaje}".encode('utf-8'))
    return mensaje

# Mensaje de abandono de chat y cerrar sesion del socket

def abandonar_chat(socket_cliente):
    usuario = clientes[socket_cliente]
    del clientes[socket_cliente]
    del direcciones[socket_cliente]
    del nombres_sockets[usuario]  # Eliminar la referencia del nombre de usuario y su socket
    broadcast(f"{usuario} ha abandonado el chat.")
    print(f"{usuario} ha abandonado el chat.")
    
# verificar si el usuario ya esta conectado
def verificar_usuario_conectado(usuario):
    if usuario in nombres_sockets:
        return True
    else:
        return False

# Manejo de conexiones entrantes

def aceptar_conexiones():
    while True:
        cliente_socket, cliente_direccion = server.accept()      
        print(f"Conexión entrante desde {cliente_direccion}")
        nombre_usuario = cliente_socket.recv(1024).decode('utf-8')
        # verificar si el usuario ya esta conectado
        if verificar_usuario_conectado(nombre_usuario):
            print("El usuario ya esta conectado")
            break
        clientes[cliente_socket] = nombre_usuario
        direcciones[cliente_socket] = cliente_direccion
        nombres_sockets[nombre_usuario] = cliente_socket  # Asociar el nombre de usuario con su socket
        print(f"Nombre de usuario: {nombre_usuario}")
        enviar_mensaje(cliente_socket, f"Se conecto al servidor '{cliente_direccion}'.\n")
        broadcast(f"{nombre_usuario} se ha unido al chat.\n")
        enviar_lista_usuarios(cliente_socket)
        thread_cliente = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
        thread_cliente.start()

def manejar_cliente(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje:
                usuario_origen = clientes[cliente]
                if "chao" in mensaje.lower():
                    abandonar_chat(cliente)
                    break
                if mensaje.startswith("!"):
                    usuario_destino = mensaje[1:]
                    verify_user = verificar_usuario_conectado(usuario_destino)
                    if verify_user:
                        mensaje = enviar_mensaje(cliente, f"Iniciando chat con: '{usuario_destino}' .")
                        guardar_datos_mensaje(usuario_origen, usuario_destino, mensaje)
                    else:
                        mensaje = enviar_mensaje(cliente, f"El usuario '{usuario_destino}' no está conectado.")
                        guardar_datos_mensaje(usuario_origen, usuario_destino, mensaje)
                        break
                elif mensaje.startswith("@"):
                    destinatario, mensaje_enviar = mensaje.split(": ", 1)
                    destinatario = destinatario[1:]
                    if destinatario in nombres_sockets:
                        socket_destinatario = nombres_sockets[destinatario]
                        mensaje = enviar_mensaje(socket_destinatario, f">>Mensaje de @{usuario_origen}: {mensaje_enviar}")
                        guardar_datos_mensaje(usuario_origen, destinatario, mensaje)
                    else:
                        mensaje = enviar_mensaje(cliente, f"El usuario '{destinatario}' no existe o no está conectado.")
                        guardar_datos_mensaje(usuario_origen, destinatario, mensaje)
                else:
                    mensaje = enviar_mensaje(cliente, f"No se logro enviar el mensaje a el usuario {usuario_origen}.")
                    guardar_datos_mensaje(usuario_origen, usuario_origen, mensaje)
                    pass
        except ConnectionResetError:
            abandonar_chat(cliente)
            break

if __name__ == "__main__":
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 5555))
        server.listen(5)
        print("Esperando conexiones...")
        aceptar_hilos = threading.Thread(target=aceptar_conexiones)
        aceptar_hilos.start()

        while True:
            pass  # Mantener el servidor en ejecución

    except KeyboardInterrupt:
        detener_servidor()

    except Exception as e:
        print(f"Error al iniciar el servidor: {e}")
        detener_servidor()