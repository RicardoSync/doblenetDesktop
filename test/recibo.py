import mysql.connector
from datetime import datetime, timedelta

# Configura la conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="dni",
    password="MinuzaFea265/",
    database="alpha"
)

# Crea un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Función para buscar un cliente por su ID
def buscar_cliente_por_id(id_cliente):
    try:
        # Consulta SQL para buscar el cliente por su ID
        sql_select = "SELECT * FROM clientes WHERE id = %s"
        cursor.execute(sql_select, (id_cliente,))
        cliente = cursor.fetchone()  # Obtiene el primer registro encontrado

        if cliente:
            return cliente
        else:
            print(f"No se encontró ningún cliente con el ID {id_cliente}.")
            return None

    except mysql.connector.Error as error:
        print(f"Error al buscar cliente: {error}")
        return None

# Función para registrar un pago y actualizar la fecha de próximo pago
def registrar_pago(id_cliente, mensualidad):
    try:
        # Obtén la fecha actual y calcula el próximo pago
        fecha_actual = datetime.now().date()
        fecha_proximo_pago = fecha_actual + timedelta(days=31)

        # Actualiza la fecha de próximo pago en la tabla clientes
        sql_update_cliente = "UPDATE clientes SET ProximoPago = %s WHERE id = %s"
        cursor.execute(sql_update_cliente, (fecha_proximo_pago, id_cliente))
        conexion.commit()

        # Registra el pago en la tabla pagos
        sql_insert_pago = "INSERT INTO pagos (NombreCliente, Mensualidad, FechaPago) VALUES (%s, %s, %s)"
        cursor.execute(sql_insert_pago, (cliente[1], mensualidad, fecha_actual))  # cliente[1] es el Nombre del cliente
        conexion.commit()

        print(f"Pago registrado exitosamente para el cliente {cliente[1]}.")
        print(f"Próximo Pago actualizado a: {fecha_proximo_pago}")

    except mysql.connector.Error as error:
        print(f"Error al registrar el pago: {error}")

# ID del cliente a buscar (aquí puedes cambiar el ID según tu base de datos)
id_cliente_buscar = 5

# Busca el cliente por su ID
cliente = buscar_cliente_por_id(id_cliente_buscar)

if cliente:
    # Mostrar información del cliente encontrado
    print("Información del cliente encontrado:")
    print(f"ID: {cliente[0]}")
    print(f"Nombre: {cliente[1]}")
    print(f"Dirección: {cliente[2]}")
    print(f"Teléfono: {cliente[3]}")
    print(f"Equipos: {cliente[4]}")
    print(f"IP: {cliente[5]}")
    print(f"Velocidad: {cliente[6]} Mbps")
    print(f"Fecha de Instalación: {cliente[7]}")
    print(f"Próximo Pago: {cliente[8]}")
    print(f"Mensualidad: {cliente[9]}")

    # Solicitar el registro del pago
    mensualidad_pago = float(input("Ingrese la mensualidad a pagar: "))

    # Registrar el pago y actualizar la fecha de próximo pago
    registrar_pago(cliente[0], mensualidad_pago)  # cliente[0] es el ID del cliente

# Cierra el cursor y la conexión
if conexion.is_connected():
    cursor.close()
    conexion.close()
    print("Conexión a MySQL cerrada.")
