# Importamos las librerías necesarias
import asyncio
from autenticacion import iniciar_sesion, cerrar_sesion
from recuperar_mensajes import obtener_mensajes
from escuchar_mensajes import escuchar_mensajes
from enviar_mensajes import reenviar_mensajes

# Iniciamos la sesión del cliente y ejecutamos las funciones
if __name__ == "__main__":
    # Pedimos al usuario que ingrese su número de teléfono
    numero_telefono = "+18299281554"

    loop = asyncio.get_event_loop()
    client = loop.run_until_complete(iniciar_sesion(numero_telefono))

    # Mostramos el último mensaje del canal
    print("Mostrando último mensaje del canal...")
    loop.run_until_complete(obtener_mensajes(client))

    # Reenviamos los mensajes entre canales
    print("Reenviando mensajes entre canales...")
    loop.run_until_complete(reenviar_mensajes(client))

    # Escuchamos los mensajes del chat y cerramos la sesión del cliente al terminar
    try:
        loop.run_until_complete(escuchar_mensajes(client))
    finally:
        loop.run_until_complete(cerrar_sesion(client))


