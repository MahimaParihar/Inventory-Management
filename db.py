import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = 'mahima',
        password = 'mahima1327',
        database = 'inventry'
    )