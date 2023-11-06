import psycopg2
import json

# Carga la informacion de conexion desde el archivo JSON
def load_db_credentials():
    with open('utils/credentials_db.json') as file:
        return json.load(file)

# Establece una conexion a la base de datos
def connect_to_db():
    credentials = load_db_credentials()
    conn = psycopg2.connect(
        host=credentials['host'],
        database=credentials['database'],
        user=credentials['user'],
        password=credentials['password']
    )
    return conn

# Inserta un nuevo usuario en la tabla users
def insert_user(username, password, full_name):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, full_name) VALUES (%s, %s, %s)", (username, password, full_name))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error mientras insertaba datos de usuario:", error)
    finally:
        cursor.close()
        conn.close()

# Obtiene la informacion de un usuario por su nombre de usuario
def get_user_by_username(username):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,)) # Se define con , al final para que sea una tupla
        user = cursor.fetchone()
        return user
    except (Exception, psycopg2.Error) as error:
        print("Error mientras recuperaba los datos del usuario por username:", error)
    finally:
        cursor.close()
        conn.close()

# Obtiene la informacion de un usuario por su ID
def get_user_by_id(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,)) # Se define con , al final para que sea una tupla
        user = cursor.fetchone()
        return user
    except (Exception, psycopg2.Error) as error:
        print("Error mientras recuperaba los datos del usuario por ID:", error)
    finally:
        cursor.close()
        conn.close()

# Inserta un mensaje en la tabla conversations
def insert_message(sender_id, receiver_id, message_text):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO conversations (user1_id, user2_id, messages) VALUES (%s, %s, ARRAY[%s])", (sender_id, receiver_id, message_text))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error mientras insertaba mensaje de la conversacion:", error)
    finally:
        cursor.close()
        conn.close()

# Obtiene todos los mensajes entre dos usuarios
def get_messages_between_users(user1_id, user2_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM conversations WHERE (user1_id = %s AND user2_id = %s) OR (user1_id = %s AND user2_id = %s)", (user1_id, user2_id, user2_id, user1_id))
        messages = cursor.fetchall()
        return messages
    except (Exception, psycopg2.Error) as error:
        print("Error mientras recuperaba los datos de mensaje entre usuarios:", error)
    finally:
        cursor.close()
        conn.close()

# Marca una conversacion como finalizada cuando un usuario abandona el chat
def mark_conversation_as_ended(user1_id, user2_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE conversations SET ended = TRUE WHERE (user1_id = %s AND user2_id = %s) OR (user1_id = %s AND user2_id = %s)", (user1_id, user2_id, user2_id, user1_id))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error mientras marcaba como finalizada la conversacion:", error)
    finally:
        cursor.close()
        conn.close()

# Obtiene una lista de todos los usuarios registrados
def get_all_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return users
    except (Exception, psycopg2.Error) as error:
        print("Error mientras recuperaba los datos de todos los usuarios:", error)
    finally:
        cursor.close()
        conn.close()

# Cierra la conexion a la base de datos
def close_db_connection():
    conn = connect_to_db()
    conn.close()
