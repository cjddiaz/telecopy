# Importamos las librerías necesarias
import asyncio
from telethon.sync import TelegramClient

# Definimos la constante con el ID del chat del que queremos obtener los mensajes
CHAT_ID = -1001689323367

# Definimos la función que obtiene los mensajes del chat
async def obtener_mensajes(client):
    # Obtenemos el último mensaje del chat
    mensajes = await client.get_messages(CHAT_ID, limit=1)
    # Recorremos los mensajes obtenidos e imprimimos su texto
    for mensaje in mensajes:
        print(mensaje.text)

# Iniciamos la sesión del cliente
if __name__ == "__main__":
    from autenticacion import iniciar_sesion

    # Pedimos al usuario que ingrese su número de teléfono
    numero_telefono = input("Ingrese su número de teléfono con código de país (ejemplo: +1234567890): ")

    loop = asyncio.get_event_loop()
    client = loop.run_until_complete(iniciar_sesion(numero_telefono))

    # Ejecutamos la función que obtiene los mensajes del chat
    loop.run_until_complete(obtener_mensajes(client))

    # Cerramos la sesión del cliente
    client.disconnect()
