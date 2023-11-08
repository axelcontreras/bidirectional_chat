# bidirectional_chat
Sistema de chat bidireccional en Python con sockets. El servidor actua como base de datos PostgreSQL para almacenar conversaciones, y el cliente permite enviar/recibir mensajes. Implementacion basica para comunicacion en tiempo real.


# Estructura de archivos
- /chat_app
    - server.py
    - client.py
    - db_interaction.py
    - utils/
        - credentials_db.json
    - requirements.txt

### utils/credentials_db.json 

Archivo que almacena las credenciales de la base de datos (host, nombre de usuario, contraseña, etc.) en formato JSON para la conexion.


## Funciones por archivo:

# Server.py

Este script (`server.py`) presenta un servidor de chat implementado en Python haciendo uso de sockets para permitir la comunicación entre múltiples clientes. Permite la conexión de varios usuarios, el intercambio de mensajes, la gestión de conexiones y el almacenamiento de conversaciones en una base de datos.

## Funcionamiento

El script crea un servidor que escucha conexiones entrantes a través de un socket TCP en el puerto 5555 en localhost. Utiliza múltiples funciones para gestionar la interacción con los clientes:

- **Función de broadcast:** Envía mensajes a todos los clientes conectados.
- **Lista de usuarios conectados:** Permite obtener una lista de los usuarios actualmente conectados al servidor.
- **Envío de mensajes entre usuarios:** Facilita el envío de mensajes entre usuarios conectados y gestiona su almacenamiento en la base de datos.

El servidor maneja las conexiones entrantes, recopila información de los usuarios, y gestiona la comunicación entre ellos, permitiendo conversaciones públicas y privadas.

## Uso

Para ejecutar el servidor:

1. Ejecuta el script `server.py`.
2. Los clientes pueden conectarse al servidor utilizando un cliente adecuado que se comunique a través del mismo protocolo.


### client.py

El script `client.py` es un cliente de chat implementado en Python que utiliza sockets para conectarse a un servidor de chat, permitiendo a los usuarios intercambiar mensajes de texto.

## Funcionamiento

Este cliente permite la conexión a un servidor de chat mediante el uso de sockets. Las funciones principales incluyen:

- **Envío de mensajes:** Permite enviar mensajes al servidor y a otros usuarios conectados.
- **Recepción de mensajes:** Escucha y muestra mensajes recibidos del servidor y de otros usuarios.

## Uso

Para utilizar el cliente de chat:

1. Ejecuta el script `client.py`.
2. Ingresa la dirección IP del servidor al que te quieres conectar.
3. Proporciona un puerto para el cliente.
4. Introduce un nombre de usuario para identificarte en el chat.
5. Comienza a enviar mensajes a otros usuarios conectados al servidor.

El cliente permite enviar mensajes directos a usuarios específicos o mensajes generales al servidor, y cierra la conexión cuando el usuario lo solicita.


# db_interaction.py

El script `db_interact.py` proporciona funciones para interactuar con una base de datos PostgreSQL desde Python, permitiendo acciones como la verificación de usuarios, inserción de datos y recuperación de mensajes entre usuarios.

## Funciones disponibles

- **`load_db_credentials()`:** Carga las credenciales de conexión desde un archivo JSON.
- **`connect_to_db()`:** Establece una conexión a la base de datos PostgreSQL utilizando las credenciales proporcionadas.
- **`set_default_schema()`:** Establece un esquema por defecto para la conexión.
- **`user_exists(username)`:** Verifica si un usuario existe en la tabla de usuarios.
- **`insert_user(username)`:** Inserta un nuevo usuario en la tabla de usuarios.
- **`get_user_by_id(username)`:** Obtiene la información de un usuario por su nombre de usuario.
- **`insert_message(sender_id, receiver_id, message_text)`:** Inserta un mensaje en la tabla de conversaciones.
- **`get_messages_between_users(user1_id, user2_id)`:** Obtiene todos los mensajes entre dos usuarios.
- **`close_db_connection()`:** Cierra la conexión a la base de datos.

## Uso

# Requisitos:
Python 3.12: Todos los scripts están escritos en Python y requieren la versión 3.12 para funcionar correctamente.

## Bibliotecas estándar de Python:

socket
threading
time
json

## Dependencias específicas:

psycopg2: Para interactuar con bases de datos PostgreSQL.
Acceso a una base de datos PostgreSQL configurada y operativa para la interacción con db_interact.py.