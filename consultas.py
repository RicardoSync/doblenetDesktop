from connect import conexionDB


# Función para consultar clientes desde la base de datos
def consultarClientes():
    try:
        consulta = conexionDB()
        cursor = consulta.cursor()
        cursor.execute("SELECT id_cliente, nombre, apellido, direccion, telefono, email FROM clientes")
        resultado = cursor.fetchall()
    except Exception as e:
        print(f"Error al consultar clientes: {e}")
        resultado = [["Nombre fallido", "Apellido fallido", "Direccion fallida", "Telefono fallido", "Email fallido"]]
    finally:
        if cursor:
            cursor.close()
        if consulta:
            consulta.close()
    return resultado