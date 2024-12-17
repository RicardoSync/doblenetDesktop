from servidor import conexion

def consultaPaquetes():
    try:
        motor = conexion()
        cursor = motor.cursor()
        cursor.execute("SELECT nombre, velocidad, precio FROM paquetes")
        resultado = cursor.fetchall()

        cursor.close()
        motor.close()

        return resultado
    except:
        print("No podemos hacer la consulta de paquetes")


def consultarPagos():
    try:
        motor = conexion()
        cursor = motor.cursor()
        cursor.execute("SELECT nombre, plan, mensualidad, fechaDePago, proximoPago, efectivoCambio FROM pagos")
        reusltadoPago = cursor.fetchall()

        cursor.close()
        motor.close()

        return reusltadoPago
    
    except:
        print("no podemos consultar los pagos alv")


def consultarClientes():
    try:
        motor = conexion()
        cursor = motor.cursor()
        cursor.execute("SELECT nombre, direccion, telefono, paquete, proximoPago, estado FROM clientes")
        reusltadoPago = cursor.fetchall()

        cursor.close()
        motor.close()

        return reusltadoPago
    
    except:
        print("no podemos consultar los pagos alv")

def consultarEquipos():
    try:
        motor = conexion()
        cursor = motor.cursor()
        cursor.execute("SELECT nombre, modelo, descripcion FROM equipos")
        reusltadoPago = cursor.fetchall()

        cursor.close()
        motor.close()

        return reusltadoPago
    
    except:
        print("no podemos consultar los pagos alv")
