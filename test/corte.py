import mysql.connector
from datetime import datetime, timedelta
import time

# Configura la conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="dni",
    password="MinuzaFea265/",
    database="alpha"
)

# Crea un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Función para suspender un cliente
def suspender_cliente(ip):
    print(f"Suspendido cliente con IP: {ip}")

# Función para activar un cliente
def activar_cliente(nombre, ip, paquete):
    print(f"Activado cliente: {nombre}, IP: {ip}, Paquete: {paquete}")

# Función principal para verificar y gestionar clientes
def verificar_clientes():
    try:
        # Obtén la fecha actual
        fecha_actual = datetime.now().date()

        # Consulta SQL para obtener clientes con ProximoPago igual a la fecha actual
        sql_clientes = "SELECT Nombre, Ip, Velocidad FROM clientes WHERE ProximoPago = %s"
        cursor.execute(sql_clientes, (fecha_actual,))
        clientes = cursor.fetchall()

        for cliente in clientes:
            nombre = cliente[0]
            ip = cliente[1]
            paquete = cliente[2]

            # Consulta SQL para verificar si el cliente ya ha pagado
            sql_pagos = "SELECT * FROM pagos WHERE NombreCliente = %s"
            cursor.execute(sql_pagos, (nombre,))
            pago_cliente = cursor.fetchone()

            if pago_cliente:
                activar_cliente(nombre, ip, paquete)
            else:
                suspender_cliente(ip)

    except mysql.connector.Error as error:
        print(f"Error al consultar la base de datos: {error}")

# Bucle para ejecutar la función cada 10 segundos
while True:
    verificar_clientes()
    time.sleep(10)  # Espera 10 segundos antes de ejecutar nuevamente
