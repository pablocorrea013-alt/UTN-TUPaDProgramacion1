# EJERCICIO 4 - ESCAPE ROOM: LA BÓVEDA


# Se solicita el nombre del agente
agente = input("Nombre del agente: ")

# Validación del nombre
while not agente.isalpha():
    print("Error: el nombre debe contener solo letras.")
    agente = input("Nombre del agente: ")


# Variables iniciales indicadas por la consigna
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""


# Variable para controlar el bloqueo por alarma
bloqueado = False

# Contador de veces consecutivas que se elige forzar cerradura
forzar_seguidas = 0


# El juego continúa mientras se cumplan las condiciones
while (
    energia > 0
    and tiempo > 0
    and cerraduras_abiertas < 3
    and bloqueado == False
):

    # Se muestra el estado actual
    print("\n--- ESTADO DE LA BÓVEDA ---")
    print(f"Agente: {agente}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")


    # Menú de acciones
    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")


    # Validación de la opción
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese una opción válida entre 1 y 3.")
        opcion = input("Opción: ")

    opcion = int(opcion)


    # -------------------------------------------------
    # OPCIÓN 1 - FORZAR CERRADURA
    # -------------------------------------------------
    if opcion == 1:

        # Se suma una acción consecutiva de forzar
        forzar_seguidas += 1

        # Se descuentan los costos
        energia -= 20
        tiempo -= 2

        print("Intentás forzar la cerradura.")
        print("Costo: -20 energía y -2 tiempo.")


        # Regla anti-spam:
        # La tercera vez seguida activa la alarma
        # y NO abre la cerradura
        if forzar_seguidas == 3:

            alarma = True

            print("La cerradura se trabó.")
            print("¡ALARMA ACTIVADA!")

            # Se reinicia la racha
            forzar_seguidas = 0


        else:

            # Si la energía quedó por debajo de 40,
            # existe riesgo de activar la alarma
            if energia < 40:

                riesgo = input(
                    "Riesgo de alarma. Elija un número del 1 al 3: "
                )

                while (
                    not riesgo.isdigit()
                    or int(riesgo) < 1
                    or int(riesgo) > 3
                ):
                    print("Error: debe ingresar un número entre 1 y 3.")
                    riesgo = input(
                        "Riesgo de alarma. Elija un número del 1 al 3: "
                    )

                riesgo = int(riesgo)


                # Si elige 3, se activa la alarma
                if riesgo == 3:

                    alarma = True
                    print("¡ALARMA ACTIVADA!")


            # Si no hay alarma, se abre una cerradura
            if alarma == False and cerraduras_abiertas < 3:

                cerraduras_abiertas += 1

                print("¡Cerradura abierta!")


    # -------------------------------------------------
    # OPCIÓN 2 - HACKEAR PANEL
    # -------------------------------------------------
    elif opcion == 2:

        # Elegir otra opción corta la racha de forzar
        forzar_seguidas = 0

        # Se descuentan los costos
        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo del panel...")


        # Debe realizarse un for de 4 pasos
        for paso in range(1, 5):

            # Se agrega una letra al código parcial
            codigo_parcial += "A"

            print(f"Paso {paso}/4 - Código: {codigo_parcial}")


        # Al llegar a 8 caracteres se abre una cerradura
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas += 1

            print("¡Código suficiente!")
            print("Se abrió automáticamente una cerradura.")


    # -------------------------------------------------
    # OPCIÓN 3 - DESCANSAR
    # -------------------------------------------------
    elif opcion == 3:

        # Elegir descansar corta la racha de forzar
        forzar_seguidas = 0

        # Se recuperan 15 puntos de energía
        energia += 15

        # La energía no puede superar 100
        if energia > 100:
            energia = 100

        # Descansar consume 1 unidad de tiempo
        tiempo -= 1


        # Si la alarma está activa se descuentan
        # 10 puntos extra de energía
        if alarma == True:

            energia -= 10

            print("La alarma está activa: -10 energía extra.")


        print("Descansaste.")
        print("Recuperaste energía y perdiste 1 de tiempo.")


    # -------------------------------------------------
    # CONTROL DE BLOQUEO POR ALARMA
    # -------------------------------------------------

    # Si la alarma está activa y quedan 3 o menos
    # unidades de tiempo, el sistema se bloquea
    if (
        alarma == True
        and tiempo <= 3
        and cerraduras_abiertas < 3
    ):

        bloqueado = True


# -------------------------------------------------
# FIN DEL JUEGO
# -------------------------------------------------

if cerraduras_abiertas == 3:

    print("\n¡VICTORIA!")
    print(f"{agente} logró abrir la bóveda.")


elif bloqueado == True:

    print("\nDERROTA.")
    print("El sistema quedó bloqueado por la alarma.")


elif energia <= 0 or tiempo <= 0:

    print("\nDERROTA.")
    print("Te quedaste sin energía o sin tiempo.")