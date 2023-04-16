# Importamos las librerías necesarias
import asyncio
from telethon.sync import TelegramClient, events
from procesador_mensajes import procesar_mensaje

# Definimos las constantes con los IDs de los canales origen y destino
CANAL_ORIGEN = -1001987131402
CANAL_DESTINO = -1001871501682

# Definimos la función que reenvía los mensajes
async def reenviar_mensajes(client):
    # Creamos un manejador de eventos que escuche nuevos mensajes en el canal origen
    @client.on(events.NewMessage(chats=CANAL_ORIGEN))
    async def handler(event):
        mensaje = event.message
        print(mensaje.text) # Imprimimos el texto del mensaje original
        texto_procesado = procesar_mensaje(mensaje.text) # Procesamos el mensaje original
        print(texto_procesado) # Imprimimos el texto del mensaje procesado
        await client.send_message(CANAL_DESTINO, texto_procesado) # Enviamos el mensaje procesado al canal destino

    # Ejecutamos el cliente hasta que se desconecte
    await client.run_until_disconnected()

# Iniciamos la sesión del cliente
if __name__ == "__main__":
    from autenticacion import iniciar_sesion

    # Pedimos al usuario que ingrese su número de teléfono
    numero_telefono = input("Ingrese su número de teléfono con código de país (ejemplo: +1234567890): ")

    # Creamos un loop y ejecutamos la función de inicio de sesión
    loop = asyncio.get_event_loop()
    client = loop.run_until_complete(iniciar_sesion(numero_telefono))

    # Ejecutamos la función que reenvía los mensajes
    loop.run_until_complete(reenviar_mensajes(client))

