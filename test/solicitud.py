import requests

name = 'Ricardo Escobedo'
number = '4981442266'
api = '5445857'

# Usando f-strings para mejor legibilidad y eficiencia
message = f"Hola+estimado+{name}+solo+para+notificarle+que+por+favor+realice+el+pago+de+su+servicio+para+que+pueda+disfrutar+de+nuestro+servicio."
message1 = "+No+es+necesario+que+conteste+este+mensaje+ya+que+es+generado+automaticamente"

# Combinando los mensajes si es necesario
full_message = message + message1

# Construyendo la URL usando f-strings
url = "https://api.callmebot.com/whatsapp.php?phone=+52"+number+"&text="+full_message+"&apikey="+api

# Enviando la solicitud POST
response = requests.post(url)

# Opcional: Comprobando el estado de la respuesta
if response.status_code == 200:
    print("Mensaje enviado exitosamente.")
else:
    print(f"Error al enviar el mensaje. Código de estado: {response.status_code}")
