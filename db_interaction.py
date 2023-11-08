import psycopg2
import json

# Carga la informacion de conexion desde el archivo JSON
def load_db_credentials():
    with open('utiles/credentials_db.json') as file:
        return json.load(file)

# Establece una conexion a la base de datos
def connect_to_db():
    credentials = load_db_credentials()
    conn = psycopg2.connect(
        host=credentials['host'],
        database=credentials['database'],
        user=credentials['user'],
        password=credentials['password'],
    )
    return conn

# elegir el schema por defecto para la conexion
def set_default_schema():
    with open(connect_to_db()) as conn:
        with open(conn.cursor()) as cursor:
            try:
                cursor.execute("SET search_path TO chat_schema")
                conn.commit()
            except (Exception, psycopg2.Error) as error:
                print("Error mientras establecia el schema por defecto:", error)

# verifica si el usuario existe en la tabla users
def user_exists(username):
    with open(connect_to_db()) as conn:
        with open(conn.cursor()) as cursor:
            try:
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,)) # Se define con , al final para que sea una tupla
                user = cursor.fetchone()
                if user:
                    return True
                else:
                    return False
            except (Exception, psycopg2.Error):
                pass

# Inserta un nuevo usuario en la tabla users
def insert_user(username):
    with open(connect_to_db()) as conn:
        with open(conn.cursor()) as cursor:
            try:
                cursor.execute("INSERT INTO users (username, ) VALUES (%s)", (username))
                conn.commit()
            except (Exception, psycopg2.Error) as error:
                print("Error mientras insertaba datos de usuario:", error)

# # Obtiene la informacion de un usuario por su nombre de usuario
# def get_user_by_username(username):
#     with open(connect_to_db()) as conn:
#         with open(conn.cursor()) as cursor:
#             try:
#                 cursor.execute("SELECT * FROM users WHERE username = %s", (username,)) # Se define con , al final para que sea una tupla
#                 user = cursor.fetchone()
#                 return user
#             except (Exception, psycopg2.Error) as error:
#                 print("Error mientras recuperaba los datos del usuario por username:", error)

# Obtiene la informacion de un usuario por su ID
def get_user_by_id(user_id):
    with open(connect_to_db()) as conn:
        with open(conn.cursor()) as cursor:
            try:
                cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,)) # Se define con , al final para que sea una tupla
                user = cursor.fetchone()
                return user
            except (Exception, psycopg2.Error) as error:
                print("Error mientras recuperaba los datos del usuario por ID:", error)

# Inserta un mensaje en la tabla conversations
def insert_message(sender_id, receiver_id, message_text):
    with open(connect_to_db()) as conn:
        with open(conn.cursor()) as cursor:
            try:
                cursor.execute("INSERT INTO conversations (user1_id, user2_id, messages) VALUES (%s, %s, %s)", (sender_id, receiver_id, message_text))
                conn.commit()
            except (Exception, psycopg2.Error) as error:
                print("Error mientras insertaba mensaje de la conversacion:", error)

# Obtiene todos los mensajes entre dos usuarios
def get_messages_between_users(user1_id, user2_id):
    with open(connect_to_db()) as conn:
        with open(conn.cursor()) as cursor:
            try:
                cursor.execute("SELECT * FROM conversations WHERE (user1_id = %s AND user2_id = %s) ORDER BY timestamp ASC", (user1_id, user2_id, user2_id, user1_id))
                messages = cursor.fetchall()
                return messages
            except (Exception, psycopg2.Error) as error:
                print("Error mientras recuperaba los datos de mensaje entre usuarios:", error)

# Cierra la conexion a la base de datos
def close_db_connection():
    conn = connect_to_db()
    conn.close()
