import json
import paramiko

def iniciarTarea():
    # Leer el archivo JSON
    with open('comandos.json') as f:
        data = json.load(f)

    # Extraer los datos del archivo JSON
    hostname = data['hostname']
    port = data['port']
    username = data['username']
    password = data['password']
    commands = data['comandos']

    try:
        # Crear el cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)

        # Ejecutar los comandos
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            print(f"Output for command '{command}':")
            print(stdout.read().decode())
            err = stderr.read().decode()
            if err:
                print(f"Error for command '{command}': {err}")

    except Exception as e:
        print(f'Error: {e}')

    finally:
        # Cerrar la conexión SSH
        ssh.close()

iniciarTarea()
