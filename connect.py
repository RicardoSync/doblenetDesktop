import mysql.connector
from tkinter import messagebox


def conexionDB():
    try:
        conn = mysql.connector.Connect(
            host='localhost',
            user='root',
            password='MinuzaFea265/',
            database='doblenet'
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("DOBLENET", f"No podemos establecer conexion al servidor {err}")
        return "001"
    
