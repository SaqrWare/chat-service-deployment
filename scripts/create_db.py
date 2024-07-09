from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import time

# Connection parameters
hosts = ['cassandra-seed']  # Adjust with your Cassandra host
port = 9042
keyspace = "chat"

# CQL commands
cql_commands = [
    """
    CREATE KEYSPACE IF NOT EXISTS chat WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}
    AND durable_writes = true;
    """,
    """
    CREATE TABLE IF NOT EXISTS chat."user"
    (
        id         uuid PRIMARY KEY,
        created_at timestamp,
        email      text,
        first_name text,
        last_name  text,
        "password" text,
        username   text
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS chat.message
    (
        id          uuid PRIMARY KEY,
        content     text,
        created_at  timestamp,
        delivered   boolean,
        receiver_id uuid,
        sender_id   uuid
    );
    """,
    """CREATE INDEX IF NOT EXISTS ON chat.message (sender_id);""",
    """CREATE INDEX IF NOT EXISTS ON chat.message (receiver_id);""",
    """CREATE INDEX IF NOT EXISTS ON chat.message (created_at);""",
    """CREATE INDEX IF NOT EXISTS ON chat."user" (username);""",
    """CREATE INDEX IF NOT EXISTS ON chat."user" (email);"""
]

def wait_for_cassandra_ready():
    while True:
        try:
            cluster = Cluster(hosts, port=port)
            session = cluster.connect()
            print("Connected to Cassandra")
            return session
        except Exception as e:
            print("Waiting for Cassandra to be ready...", e)
            time.sleep(5)

def execute_cql_commands(session):
    for command in cql_commands:
        try:
            session.execute(command)
            print(f"Successfully executed CQL command:\n{command}")
        except Exception as e:
            print(f"Error executing CQL command:\n{command}\nError: {e}")

def main():
    session = wait_for_cassandra_ready()
    execute_cql_commands(session)

if __name__ == "__main__":
    main()