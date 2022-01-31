from flask import Flask
import psycopg2
import os

app = Flask(__name__)


def connect_to_database():
    conn_string = os.environ['DB_CONN_STRING']
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT 1")


@app.route("/")
def homepage():

    connected = True
    print('I HAVE STARTED.')

    try:
        connect_to_database()
    except psycopg2.OperationalError:
        print('Could not connect to DB')
        connected = False

    if connected:
        return f"<h1>I am connected to database!</h1>"
    else:
        return f"<h1>I am not connected to database, sorry.</h1>"