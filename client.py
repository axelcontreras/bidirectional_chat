import socket
import threading
import time

def recibir_mensajes(socket_cliente):
    try:
        while True:
            mensaje = socket_cliente.recv(1024).decode('utf-8')
            if mensaje:
                print(mensaje)
    except ConnectionResetError:
        print("Conexión perdida con el servidor.")
        return

def main():
    host = input("Ingrese la dirección IP del servidor: ") or "localhost"  # Dirección IP del servidor
    port = 5555  # Puerto del servidor
    client_port = input("Ingrese el puerto a utilizar: ")

    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_cliente.bind((host, int(client_port)))
        socket_cliente.connect((host, port))
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor.")
        return

    nombre_usuario = input("Ingrese su nombre de usuario: ")
    socket_cliente.send(nombre_usuario.encode('utf-8'))

    recibir_hilos = threading.Thread(target=recibir_mensajes, args=(socket_cliente,))
    recibir_hilos.start()
    time.sleep(1)
    try:
        while True:
            usuario_destino = input("Ingrese el nombre del usuario con el que desea chatear: ")
            socket_cliente.send(f"!{usuario_destino}".encode('utf-8'))
            time.sleep(0.1)
            mensaje = input(f"<<Mensaje a @{usuario_destino}: ")
            socket_cliente.send(f"@{usuario_destino}: {mensaje}".encode('utf-8'))

            if mensaje.lower() == "chao":
                break
        
        socket_cliente.close()
    except KeyboardInterrupt:
        print("Saliendo del chat...")
        socket_cliente.send("chao".encode('utf-8'))
        socket_cliente.close()

if __name__ == "__main__":
    main()
