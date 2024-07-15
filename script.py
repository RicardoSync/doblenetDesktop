import mysql.connector
from datetime import datetime
import json

def gestionar_pagos():
    # Cargar la configuración desde el archivo JSON
    with open('config.json') as f:
        db_config = json.load(f)

    # Función para activar clientes
    def activar(id, nombre, ip, velocidad):
        print(f"Activar: ID={id}, Nombre={nombre}, IP={ip}, Velocidad={velocidad}")

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        estado = "activado"
        update_estado = "UPDATE clientes SET estado = %s WHERE id = %s"
        cursor.execute(update_estado, (estado, id))

        cursor.close()
        conn.commit()

    # Función para suspender clientes
    def suspender(id, nombre):
        print(f"Suspender: ID={id}, Nombre={nombre}")

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        estado = "suspendido"
        update_estado = "UPDATE clientes SET estado = %s WHERE id = %s"
        cursor.execute(update_estado, (estado, id))

        cursor.close()
        conn.commit()

    # Obtener la fecha actual del PC
    fecha_actual = datetime.now().date()

    # Conectar a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    try:
        # Obtener los clientes con ProximoPago igual a la fecha actual
        query_clientes = """
        SELECT id, Nombre, Ip, Velocidad 
        FROM clientes 
        WHERE ProximoPago = %s
        """
        cursor.execute(query_clientes, (fecha_actual,))
        clientes = cursor.fetchall()

        for cliente in clientes:
            id_cliente = cliente['id']
            nombre = cliente['Nombre']
            ip = cliente['Ip']
            velocidad = cliente['Velocidad']

            # Buscar el cliente en la tabla pagos
            query_pagos = """
            SELECT * 
            FROM pagos 
            WHERE NombreCliente = %s
            """
            cursor.execute(query_pagos, (nombre,))
            pago = cursor.fetchone()

            # Llamar a activar o suspender según corresponda
            if pago:
                activar(id_cliente, nombre, ip, velocidad)
            else:
                suspender(id_cliente, nombre)

    finally:
        # Cerrar la conexión a la base de datos
        cursor.close()
        conn.close()

# Llamar a la función para ejecutar la gestión de pagos
gestionar_pagos()
