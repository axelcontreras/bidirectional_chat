-- user_id (clave primaria): Identificador único para cada usuario.
-- username: Nombre de usuario o identificador único.
-- password: Contraseña.
-- nombre: Nombre real del usuario.
-- status: Estado del usuario (online, offline, etc).

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(16) NOT NULL,
    full_name VARCHAR(200) NOT NULL,
    status VARCHAR(50) DEFAULT 'offline'
);

-- conversation_id (clave primaria): Identificador único para cada conversación.
-- user1_id y user2_id: IDs de los usuarios que participan en la conversación.
-- messages: Texto de los mensajes intercambiados.
-- ended: Indica si la conversacion ha finalizado.
-- timestamp: Fecha y hora del mensaje.

CREATE TABLE conversations (
    conversation_id SERIAL PRIMARY KEY,
    user1_id INT NOT NULL,
    user2_id INT NOT NULL,
    messages TEXT[],
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user1_id) REFERENCES users(user_id),
    FOREIGN KEY (user2_id) REFERENCES users(user_id)
);
