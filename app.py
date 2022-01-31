from flask import Flask
import psycopg2

app = Flask(__name__)


def connect_to_database():
    conn_string = "dbname='postgres-example-db' user='psqladmin@postgres-example-db-server' host='postgres-example-db-server.postgres.database.azure.com' password='newpassword123!!!!!' port='5432' sslmode='require'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT 1")


@app.route("/")
def homepage():

    connected = True

    try:
        connect_to_database()
    except psycopg2.OperationalError:
        print('Could not connect to DB')
        connected = False

    if connected:
        return f"<h1>I am connected to database!</h1>"
    else:
        return f"<h1>I am not connected to database, sorry.</h1>"