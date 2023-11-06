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

## Descripcion de cada archivo:

### server.py 

Este archivo contiene el codigo para el servidor del chat. Maneja las conexiones entrantes, la logica del chat y la interaccion con la base de datos.<br>
Aqui se implementaron las funciones para atender a multiples clientes, mostrar usuarios conectados y gestionar las conversaciones.

### client.py 

Aqui residira la logica del cliente del chat. Se encargara de establecer la conexion con el servidor, enviar y recibir mensajes, y manejar la interfaz de usuario del cliente.

### db_interaction.py 

Contendra funciones relacionadas con la interaccion con la base de datos. Manejara consultas para registrar usuarios, mensajes y cualquier interaccion relacionada con la base de datos.

### utils/credentials_db.json 

Archivo que almacena las credenciales de la base de datos (host, nombre de usuario, contraseña, etc.) en formato JSON para la conexion.

### requirements.txt 
Archivo que enumera todas las dependencias del proyecto. Puede incluir las versiones de las bibliotecas de Python que utilizas. Esto ayuda a otros desarrolladores a instalar las dependencias necesarias facilmente con pip.

## Funciones por archivo:

### server.py

- Funciones para manejar conexiones entrantes.
- Gestion de usuarios conectados.
- Logica para enviar y recibir mensajes entre los usuarios.
- Integracion con la base de datos para registrar conversaciones y usuarios.

### client.py

- Logica para conectarse al servidor.
- Manejo de la interfaz de usuario para enviar y recibir mensajes.
- Gestion de la interaccion del usuario con el chat.

### db_interaction.py

- Funciones para interactuar con la base de datos: insertar usuarios, mensajes, obtener conversaciones, etc.
- Gestion de la conexion y consultas a la base de datos.