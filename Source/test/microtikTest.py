from librouteros import connect, exceptions
from librouteros.query import Key

def connect_to_router(host, username, password, port=8728):
    try:
        return connect(username=username, password=password, host=host, port=port)
    except exceptions.TrapError as e:
        print(f"Error de API de MikroTik: {e}")
    except ConnectionRefusedError:
        print("Conexión rechazada. Asegúrate de que el servicio API esté habilitado y la IP/puerto sean correctos.")
    except Exception as e:
        print(f"Error desconocido: {e}")

# Conéctate a tu MikroTik
api = connect_to_router(
    username='admin',  # Cambia esto por tu usuario
    password='070523',  # Cambia esto por tu contraseña
    host='122.122.125.1'  # Cambia esto por la IP de tu MikroTik
)

if api:
    # Función para actualizar la velocidad de una cola específica
    def update_queue_speed(ip_address, max_limit):
        queues = api.path('queue', 'simple')
        target_queue = None

        for queue in queues.select():
            if queue.get('target') == ip_address:
                target_queue = queue
                break

        if not target_queue:
            print(f"No se encontró ninguna cola para la IP {ip_address}")
            return

        queue_id = target_queue.get('.id')
        queues.set(id=queue_id, max_limit=max_limit)
        print(f"Velocidad de la IP {ip_address} cambiada a {max_limit}")

    # Cambia la velocidad de la IP especificada
    ip_address = '122.122.126.92'  # Cambia esto por la IP que deseas modificar
    new_speed = '5M/5M'  # Cambia esto por la nueva velocidad deseada (ejemplo: '5M/5M')

    update_queue_speed(ip_address, new_speed)
