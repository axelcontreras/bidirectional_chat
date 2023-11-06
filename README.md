# bidirectional_chat
Sistema de chat bidireccional en Python con sockets. El servidor actúa como base de datos PostgreSQL para almacenar conversaciones, y el cliente permite enviar/recibir mensajes. Implementación básica para comunicación en tiempo real.


# Estructura de archivos
- /chat_app
    - server.py
    - client.py
    - db_interaction.py
    - utils/
        - credentials_db.json
    - requirements.txt

## Descripción de cada archivo:
### server.py 
Este archivo contiene el código para el servidor del chat. Manejará las conexiones entrantes, la lógica del chat y la interacción con la base de datos.<br>
Aquí se implementarán las funciones para atender a múltiples clientes, mostrar usuarios conectados y gestionar las conversaciones.

### client.py: 
Aquí residirá la lógica del cliente del chat. Se encargará de establecer la conexión con el servidor, enviar y recibir mensajes, y manejar la interfaz de usuario del cliente.

db_interaction.py: Contendrá funciones relacionadas con la interacción con la base de datos. Manejará consultas para registrar usuarios, mensajes y cualquier interacción relacionada con la base de datos.

utils/credentials_db.json: Archivo que almacena las credenciales de la base de datos (host, nombre de usuario, contraseña, etc.) en formato JSON para la conexión.

requirements.txt: Archivo que enumera todas las dependencias del proyecto. Puede incluir las versiones de las bibliotecas de Python que utilizas. Esto ayuda a otros desarrolladores a instalar las dependencias necesarias fácilmente con pip.

Funciones sugeridas en cada archivo:
server.py:
Funciones para manejar conexiones entrantes.
Gestión de usuarios conectados.
Lógica para enviar y recibir mensajes entre los usuarios.
Integración con la base de datos para registrar conversaciones y usuarios.
client.py:
Lógica para conectarse al servidor.
Manejo de la interfaz de usuario para enviar y recibir mensajes.
Gestión de la interacción del usuario con el chat.
db_interaction.py:
Funciones para interactuar con la base de datos: insertar usuarios, mensajes, obtener conversaciones, etc.
Gestión de la conexión y consultas a la base de datos.