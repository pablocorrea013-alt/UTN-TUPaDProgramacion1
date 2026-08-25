# EJERCICIO 3 - AGENDA DE TURNOS CON NOMBRES
# SIN LISTAS, DICCIONARIOS, SETS NI TUPLAS


# Se solicita el nombre del operador
operador = input("Nombre del operador: ")

# Se valida que contenga solamente letras
while not operador.isalpha():
    print("Error: el nombre debe contener solo letras.")
    operador = input("Nombre del operador: ")


# Variables para los turnos del lunes
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Variables para los turnos del martes
martes1 = ""
martes2 = ""
martes3 = ""


# Variable para controlar el cierre del sistema
salir = False


# Menú principal
while salir == False:

    print("\n--- AGENDA DE TURNOS ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")

    # Validación numérica
    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    # Validación de rango
    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")


    # -------------------------------------------------
    # OPCIÓN 1 - RESERVAR TURNO
    # -------------------------------------------------
    elif opcion == 1:

        print("\n1. Lunes")
        print("2. Martes")

        dia = input("Seleccione día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: debe elegir 1 o 2.")
            dia = input("Seleccione día: ")

        dia = int(dia)

        # Se solicita el nombre del paciente
        paciente = input("Nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Nombre del paciente: ")


        # RESERVA PARA LUNES
        if dia == 1:

            # Se controla que el paciente no esté repetido
            if (
                paciente.lower() == lunes1.lower()
                or paciente.lower() == lunes2.lower()
                or paciente.lower() == lunes3.lower()
                or paciente.lower() == lunes4.lower()
            ):
                print("Error: el paciente ya tiene un turno el lunes.")

            # Se guarda en el primer espacio libre
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado correctamente.")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente.")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente.")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el lunes.")


        # RESERVA PARA MARTES
        elif dia == 2:

            # Se controla que el paciente no esté repetido
            if (
                paciente.lower() == martes1.lower()
                or paciente.lower() == martes2.lower()
                or paciente.lower() == martes3.lower()
            ):
                print("Error: el paciente ya tiene un turno el martes.")

            # Se guarda en el primer espacio libre
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado correctamente.")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado correctamente.")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el martes.")


    # -------------------------------------------------
    # OPCIÓN 2 - CANCELAR TURNO
    # -------------------------------------------------
    elif opcion == 2:

        print("\n1. Lunes")
        print("2. Martes")

        dia = input("Seleccione día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: debe elegir 1 o 2.")
            dia = input("Seleccione día: ")

        dia = int(dia)

        paciente = input("Nombre del paciente a cancelar: ")

        while not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Nombre del paciente a cancelar: ")


        # CANCELACIÓN DEL LUNES
        if dia == 1:

            if paciente.lower() == lunes1.lower():
                lunes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes2.lower():
                lunes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes3.lower():
                lunes3 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes4.lower():
                lunes4 = ""
                print("Turno cancelado correctamente.")

            else:
                print("El paciente no posee turno el lunes.")


        # CANCELACIÓN DEL MARTES
        elif dia == 2:

            if paciente.lower() == martes1.lower():
                martes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == martes2.lower():
                martes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == martes3.lower():
                martes3 = ""
                print("Turno cancelado correctamente.")

            else:
                print("El paciente no posee turno el martes.")


    # -------------------------------------------------
    # OPCIÓN 3 - VER AGENDA DEL DÍA
    # -------------------------------------------------
    elif opcion == 3:

        print("\n1. Lunes")
        print("2. Martes")

        dia = input("Seleccione día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: debe elegir 1 o 2.")
            dia = input("Seleccione día: ")

        dia = int(dia)


        # MOSTRAR LUNES
        if dia == 1:

            print("\n--- AGENDA DEL LUNES ---")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")


        # MOSTRAR MARTES
        elif dia == 2:

            print("\n--- AGENDA DEL MARTES ---")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")


    # -------------------------------------------------
    # OPCIÓN 4 - RESUMEN GENERAL
    # -------------------------------------------------
    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0

        # Se cuentan los turnos ocupados del lunes
        if lunes1 != "":
            ocupados_lunes += 1

        if lunes2 != "":
            ocupados_lunes += 1

        if lunes3 != "":
            ocupados_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1


        # Se cuentan los turnos ocupados del martes
        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1


        # Se calculan los disponibles
        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes


        print("\n--- RESUMEN GENERAL ---")

        print(f"Lunes - Ocupados: {ocupados_lunes}")
        print(f"Lunes - Disponibles: {disponibles_lunes}")

        print(f"Martes - Ocupados: {ocupados_martes}")
        print(f"Martes - Disponibles: {disponibles_martes}")


        # Se determina qué día tiene más turnos ocupados
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")

        else:
            print("Hay empate entre Lunes y Martes")


    # -------------------------------------------------
    # OPCIÓN 5 - CERRAR SISTEMA
    # -------------------------------------------------
    elif opcion == 5:

        print("Sistema cerrado.")
        salir = True