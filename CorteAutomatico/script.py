import mysql.connector
from datetime import datetime
import schedule
import time
import paramiko

# Configuración de la conexión a la base de datos
db_config = {
    'user': 'dni',
    'password': 'MinuzaFea265/',
    'host': 'localhost',
    'database': 'alpha'
}

def adjust_bandwidth(target_ip, new_max_limit, hostname, username, password):
    # Puerto SSH, generalmente es 22
    port = 22

    # Comando para ajustar el ancho de banda utilizando la IP
    command = f'/queue simple set [find target="{target_ip}/32"] max-limit={new_max_limit}'

    # Crear una instancia del cliente SSH
    client = paramiko.SSHClient()

    # Agregar automáticamente la clave del servidor si no está en la lista de known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conectarse al dispositivo
        client.connect(hostname, port, username, password)

        # Ejecutar el comando para ajustar el ancho de banda
        stdin, stdout, stderr = client.exec_command(command)

        # Leer y mostrar la salida del comando, si es necesario
        output = stdout.read().decode()
        errors = stderr.read().decode()

        if output:
            print(f"Output: {output}")
        if errors:
            print(f"Errors: {errors}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Cerrar la conexión
        client.close()


# Función para activar clientes
def activar(id, nombre, ip, velocidad):
    print(f"Activando: ID={id}, Nombre={nombre}, IP={ip}, Velocidad={velocidad}")

# Función para suspender clientes
def suspender(id, nombre, ip):
    print(f"Suspender: ID={id}, Nombre={nombre}, IP={ip}")
    new_max_limit = "1k/1k"
    hostname = "122.122.125.1"
    username = "admin"
    password = "070523"
    adjust_bandwidth(ip, new_max_limit, hostname, username, password)

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
                suspender(id_cliente, nombre, ip)

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
