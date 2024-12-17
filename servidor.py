import mysql.connector

def conexion():
    try:
        conexionServidor = mysql.connector.Connect(
            host="200.234.224.17",
            port=3389,
            user="ciso",
            password="ciso",
            database="doblenet"
        )
        return conexionServidor
    
    except mysql.connector.Error as err:
        print(f"No podemos establecer una conexion {err}")
        return None
    
