import pywhatkit as kit

phone_number = "wa.me/+524962006665"
message = "Hola, este es un mensaje automático de prueba."

# Enviar el mensaje de WhatsApp inmediatamente (con unos segundos de espera para abrir WhatsApp Web)
kit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True, close_time=3)
