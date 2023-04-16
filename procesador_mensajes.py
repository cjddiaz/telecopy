def procesar_mensaje(message):
    # Convertir el mensaje en texto y quitar comas
    texto = message
    texto = texto.replace(",", "")

    # Separar el texto en líneas
    salto_de_linea = "\n"
    lineas = texto.split(salto_de_linea)

    # Definir variables para almacenar información
    coin, direction, exchange, leverage = "", "", "", ""
    entry, targets, stop_loss = "", "", ""

    # Recorrer cada línea y buscar información específica
    for linea in lineas:
        # Buscar el nombre de la moneda o par de trading
        if "Coin:" in linea or "COIN:" in linea or "Pair:" in linea or "PAIR:" in linea or "#:" in linea or "✴️ Pair:" in linea:
            coin = linea.split(":")[1].strip()
        # Buscar el apalancamiento
        elif "Leverage:" in linea or "💫 Leverage:" in linea:
            leverage = linea.split(":")[1].strip()
        # Buscar el precio de entrada
        elif "ENTRY:" in linea or "ENTRY :" in linea or "🟩 Entry :" in linea:
            entry = linea.split(":")[1].strip()
        # Buscar los objetivos de precio
        elif "TARGETS:" in linea:
            targets = linea.split(":")[1].strip()
        elif "🔘" in linea or "☑️" in linea:
            # Si se encuentra un objetivo de precio en varias líneas, agregarlos juntos
            if not targets:
                targets = linea.split(" ")[-1]
            else:
                targets += " - " + linea.split(" ")[-1]
        # Buscar el stop loss
        elif "STOP LOSS:" in linea or "🚫STOP LOSS:" in linea or "⛔️ Stop loss:" in linea or "SL" in linea or "Sl" in linea:
            stop_loss = linea.split(":")[1].strip()

    # Separar los objetivos de precio y precios de entrada en listas
    target_array = targets.split(" - ")
    entry_array = entry.split(" - ")

    # Encontrar la dirección del trade (LONG o SHORT)
    direction = lineas[1].split(":")[1].strip()
    # Agregar un apalancamiento por defecto (en este caso, 20x)
    leverage = " Cross 20x"

    # Obtener el precio de entrada y el primer objetivo de precio
    ult_entry_array = len(entry_array) - 1
    entry = entry_array[0] + " - " + entry_array[ult_entry_array]
    entry_unico = float(entry_array[0])
    target_unico = float(target_array[0])

    # Crear una lista vacía para almacenar los objetivos de precio
    sucesion = [0] * 8

    # Definir la dirección
    if target_array[0] > entry_array[0]:
        direction="LONG"
    elif entry_array[0] > target_array[0]:
        direction="SHORT"

    stop_loss = float(stop_loss)

    # Determinar si el stop loss y los objetivos de precio son parametrizables
    parametrizable = False

    # Si los valores son parametrizables, calcularlos usando una fórmula
    if parametrizable == True:
        if direction == "LONG":
            # Calcular los objetivos de precio usando la fórmula de crecimiento exponencial
            for n in range(2, 8):
                sucesion[n] = entry_unico * 1.005 ** (n - 1)
            # Calcular el stop loss
            stop_loss = entry_unico * 0.75
        elif direction == "SHORT":
            # Calcular los objetivos de precio usando la fórmula de decrecimiento exponencial
            for n in range(2, 8):
                sucesion[n] = entry_unico * 0.995 ** (n - 1)
            # Calcular el stop loss
            stop_loss = entry_unico * 1.25

    # Si los valores no son parametrizables, usar objetivos de precio predefinidos
    else:
        if direction == "LONG":
            # Calcular los objetivos de precio usando la fórmula de crecimiento exponencial
            for n in range(1, 7):
                sucesion[n] = target_unico * 1.005 ** (n - 1)
        elif direction == "SHORT":
            # Calcular los objetivos de precio usando la fórmula de decrecimiento exponencial
            for n in range(1, 7):
                sucesion[n] = target_unico * 0.995 ** (n - 1)

    # Crear el texto final del mensaje
    texto_final = f"Par: {coin}\nDirection: {direction}\nLeverage: {leverage}\n\nEntry: {entry}\n\n"

    zz = 1

    # Si los valores son parametrizables, agregar los objetivos de precio y el stop loss al texto final
    if parametrizable == True:
        if entry_unico < 1000:
            for n in range(2, 8):
                texto_final += f"TARGET {zz}: {sucesion[n]:.4f}\n"
                zz = zz + 1
        else:
            for n in range(2, 8):
                texto_final += f"TARGET {zz}: {sucesion[n]:,.0f}\n"
                zz = zz + 1

    # Si los valores no son parametrizables, agregar los objetivos de precio predefinidos al texto final
    else:
        if entry_unico < 1000:
            for n in range(1, 7):
                texto_final += f"TARGET {zz}: {sucesion[n]:.4f}\n"
                zz = zz + 1
        else:
            for n in range(1, 7):
                texto_final += f"TARGET {zz}: {sucesion[n]:,.0f}\n"
                zz = zz + 1

    # Agregar el stop loss al texto final
    texto_final += f"\nSTOP LOSS: {stop_loss:.4f}" if stop_loss < 1000 else f"\nSTOP LOSS: {stop_loss:,.2f}"

    # Devolver el texto final
    return texto_final