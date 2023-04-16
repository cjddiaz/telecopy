usararchivo = True
if usararchivo == True:
    # Importamos las librerías necesarias
    import sys
    import asyncio
    from telethon.sync import TelegramClient
    from telethon.errors import SessionPasswordNeededError

    # Definimos las constantes con el ID y la clave de la API de Telegram
    API_ID = 20559228
    API_HASH = "6546910b0f0890d39f2f8a8c5e39ca90"

    # Definimos la función de inicio de sesión
    async def iniciar_sesion(numero_telefono):
        # Creamos un cliente de Telegram con el número de teléfono, el ID y la clave de la API
        client = TelegramClient(numero_telefono, API_ID, API_HASH)
        await client.connect()

        # Si el usuario no está autorizado, solicitamos el código de verificación o la contraseña de dos factores
        if not await client.is_user_authorized():
            try:
                await client.send_code_request(numero_telefono)
                code = input("Ingrese el código de verificación: ")
                await client.sign_in(numero_telefono, code)
            except SessionPasswordNeededError:
                password = input("Se requiere contraseña de la cuenta de dos factores: ")
                await client.sign_in(password=password)

        # Devolvemos el cliente de Telegram autenticado
        return client

    # Definimos la función de cierre de sesión
    async def cerrar_sesion(client):
        await client.disconnect()

    # Iniciamos la sesión del cliente
    if __name__ == "__main__":
        numero_telefono = input("Ingrese su número de teléfono con código de país (ejemplo: +1234567890): ")

        loop = asyncio.get_event_loop()
        client = loop.run_until_complete(iniciar_sesion(numero_telefono))
        print("Sesión iniciada correctamente.")
        loop.run_until_complete(cerrar_sesion(client))

else:

    # Importamos las librerías necesarias
    import sys
    import asyncio
    from telethon.sync import TelegramClient
    from telethon.errors import SessionPasswordNeededError
    from telethon.sessions import MemorySession

    # Definimos las constantes con el ID y la clave de la API de Telegram
    API_ID = 20559228
    API_HASH = "6546910b0f0890d39f2f8a8c5e39ca90"

    # Definimos la función de inicio de sesión
    async def iniciar_sesion(numero_telefono):
        # Creamos un objeto MemorySession para almacenar la sesión en memoria
        session = MemorySession()
        
        # Creamos un cliente de Telegram con el número de teléfono, el ID y la clave de la API
        client = TelegramClient(session, API_ID, API_HASH)
        await client.connect()

        # Si el usuario no está autorizado, solicitamos el código de verificación o la contraseña de dos factores
        if not await client.is_user_authorized():
            try:
                await client.send_code_request(numero_telefono)
                code = input("Ingrese el código de verificación: ")
                await client.sign_in(numero_telefono, code)
            except SessionPasswordNeededError:
                password = input("Se requiere contraseña de la cuenta de dos factores: ")
                await client.sign_in(password=password)

        # Devolvemos el cliente de Telegram autenticado
        return client

    # Definimos la función de cierre de sesión
    async def cerrar_sesion(client):
        await client.disconnect()

    # Iniciamos la sesión del cliente
    if __name__ == "__main__":
        numero_telefono = input("Ingrese su número de teléfono con código de país (ejemplo: +1234567890): ")

        loop = asyncio.get_event_loop()
        client = loop.run_until_complete(iniciar_sesion(numero_telefono))
        print("Sesión iniciada correctamente.")
        loop.run_until_complete(cerrar_sesion(client))


