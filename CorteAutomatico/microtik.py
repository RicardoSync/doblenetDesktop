import paramiko

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

# Uso de la función
hostname = '192.168.88.1'
username = 'admin'
password = 'password'
target_ip = '192.168.88.10'  # IP de la simple queue que quieres modificar
new_max_limit = '1M/1M'  # Nueva velocidad en formato rx/tx

adjust_bandwidth(target_ip, new_max_limit, hostname, username, password)
