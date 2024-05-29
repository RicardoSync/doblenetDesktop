import mysql.connector
from datetime import datetime
import schedule
import time

# Configuración de la conexión a la base de datos
db_config = {
    'user': 'dni',
    'password': 'MinuzaFea265/',
    'host': 'localhost',
    'database': 'alpha'
}

# Función para activar clientes
def activar(id, nombre, ip, velocidad):
    print(f"Activando: ID={id}, Nombre={nombre}, IP={ip}, Velocidad={velocidad}")

# Función para suspender clientes
def suspender(id, nombre):
    print(f"Suspender: ID={id}, Nombre={nombre}")

    cliente_id = id
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    estado = "suspendido"
    update_estado = "UPDATE clientes SET estado = %s WHERE id = %s"
    cursor.execute(update_estado, (estado, cliente_id))
    conn.commit()
    cursor.close()
    conn.close()

# Función principal que se ejecuta cada 10 segundos
def verificar_pagos():
    # Obtener la fecha actual del PC
    fecha_actual = datetime.now().date()

    # Conectar a la base de datos
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

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
        connection.close()

# Programar la función para que se ejecute cada 10 segundos
schedule.every(10).seconds.do(verificar_pagos)

# Ejecutar el scheduler en un bucle infinito
while True:
    schedule.run_pending()
    time.sleep(1)
