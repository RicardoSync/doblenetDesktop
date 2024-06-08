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

# Datos del cliente (aquí puedes modificar según tus datos)
nombre = "TUNDERBILD"
direccion = "123 Calle Principal"
telefono = "123-456-7890"
equipos = 1
ip = "122.122.126.98"
velocidad = "100M/25M"  # en Mbps
mensualidad = 50.00  # por ejemplo

# Obtén la fecha de instalación actual y la fecha de próximo pago
fecha_instalacion = datetime.now().date()
fecha_proximo_pago = fecha_instalacion + timedelta(days=31)

# Prepara la consulta SQL para insertar un nuevo cliente
sql_insert = """
    INSERT INTO clientes 
    (Nombre, Direccion, Telefono, Equipos, Ip, Velocidad, FechaInstalacion, ProximoPago, Mensualidad) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Datos a insertar en la tabla
datos_cliente = (nombre, direccion, telefono, equipos, ip, velocidad, fecha_instalacion, fecha_proximo_pago, mensualidad)

try:
    # Ejecuta la consulta SQL
    cursor.execute(sql_insert, datos_cliente)

    # Confirma la transacción
    conexion.commit()

    print("Cliente registrado exitosamente.")
    print(f"Fecha de Instalación: {fecha_instalacion}")
    print(f"Próximo Pago: {fecha_proximo_pago}")

except mysql.connector.Error as error:
    print(f"Error al insertar cliente: {error}")

finally:
    # Cierra el cursor y la conexión
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión a MySQL cerrada.")

