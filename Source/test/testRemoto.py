import mysql.connector
from mysql.connector import Error

def test_mysql_connection(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado al servidor MySQL versión {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Conectado a la base de datos: {record[0]}")
            cursor.close()
        else:
            print("No se pudo conectar al servidor MySQL")
    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión con MySQL cerrada")

# Configuración de conexión
host = "122.122.126.79"
user = "dni"
password = "MinuzaFea265/"
database = "alpha"

# Ejecutar prueba de conexión
test_mysql_connection(host, user, password, database)
