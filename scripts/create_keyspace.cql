CREATE KEYSPACE chat WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}
                      AND durable_writes = true;
CREATE TABLE chat."user"
(
    id         uuid PRIMARY KEY,
    created_at timestamp,
    email      text,
    first_name text,
    last_name  text,
    "password" text,
    username   text
);

CREATE TABLE chat.message
(
    id          uuid PRIMARY KEY,
    content     text,
    created_at  timestamp,
    delivered   boolean,
    receiver_id uuid,
    sender_id   uuid
);

// indexes
CREATE INDEX IF NOT EXISTS ON chat.message (sender_id);
CREATE INDEX IF NOT EXISTS ON chat.message (receiver_id);
CREATE INDEX IF NOT EXISTS ON chat.message (created_at);
CREATE INDEX IF NOT EXISTS ON chat."user" (username);
CREATE INDEX IF NOT EXISTS ON chat."user" (email);