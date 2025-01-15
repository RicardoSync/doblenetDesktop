from connect import conexionDB
from tkinter import messagebox
#funcion para insertar un cliente
def insertarCliente(nombre, apellido, direccion, telefono, email):
    try:
        motor = conexionDB()
        cursor = motor.cursor()
        sql = """
        INSERT INTO clientes (nombre, apellido, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nombre, apellido, direccion, telefono, email)
        cursor.execute(sql, valores)
        motor.commit()
        cursor.close()
        messagebox.showinfo("DOBLENET", "Cliente registrado de manera exitosa!!")
    
    except Exception as err:
        messagebox.showerror("DOBLENET", f"No podemos almacenar el cliente {err}")