# Importamos las librerías necesarias
import asyncio
from telethon.sync import TelegramClient, events

# Definimos la constante con el ID del chat del que queremos escuchar los mensajes
CHAT_ID = -1001689323367

# Definimos la función que escucha los mensajes del chat
async def escuchar_mensajes(client):
    # Creamos un manejador de eventos que escuche nuevos mensajes en el chat
    @client.on(events.NewMessage(chats=CHAT_ID))
    async def handler(event):
        print(event.message.text) # Imprimimos el texto del mensaje

    # Ejecutamos el cliente hasta que se desconecte
    await client.run_until_disconnected()

# Iniciamos la sesión del cliente
if __name__ == "__main__":
    from autenticacion import iniciar_sesion

    # Pedimos al usuario que ingrese su número de teléfono
    numero_telefono = input("Ingrese su número de teléfono con código de país (ejemplo: +1234567890): ")

    loop = asyncio.get_event_loop()
    client = loop.run_until_complete(iniciar_sesion(numero_telefono))

    # Ejecutamos la función que escucha los mensajes del chat
    loop.run_until_complete(escuchar_mensajes(client))


