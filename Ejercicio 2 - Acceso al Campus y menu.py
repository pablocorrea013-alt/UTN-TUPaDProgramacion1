# EJERCICIO 2 - ACCESO AL CAMPUS Y MENÚ SEGURO


# Credenciales correctas definidas por la consigna
usuario_correcto = "alumno"
clave_correcta = "python123"


# Variables para controlar los intentos y el acceso
intentos = 0
acceso = False


# Se permiten como máximo 3 intentos
while intentos < 3 and acceso == False:

    # Se solicita el usuario mostrando el número de intento
    usuario = input(f"Intento {intentos + 1}/3 - Usuario: ")

    # Se solicita la clave
    clave = input("Clave: ")

    # Se comprueba si el usuario y la clave son correctos
    if usuario == usuario_correcto and clave == clave_correcta:

        # Si son correctos, se permite el acceso
        acceso = True
        print("Acceso concedido.")

    else:

        # Si son incorrectos, se suma un intento
        intentos += 1
        print("Error: credenciales inválidas.")


# Si no consiguió ingresar después de los intentos
if acceso == False:

    print("Cuenta bloqueada")


# Si consiguió ingresar correctamente
if acceso == True:

    # Variable que controla la salida del menú
    salir = False

    # El menú se repite mientras salir sea False
    while salir == False:

        # Se muestran las opciones
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        # Se solicita una opción
        opcion = input("Opción: ")


        # Se valida que la opción sea un número
        while not opcion.isdigit():

            print("Error: ingrese un número válido.")

            opcion = input("Opción: ")


        # Se convierte la opción de texto a número entero
        opcion = int(opcion)


        # Se comprueba si la opción está fuera del rango 1 a 4
        if opcion < 1 or opcion > 4:

            print("Error: opción fuera de rango.")


        # OPCIÓN 1 - Ver estado de inscripción
        elif opcion == 1:

            print("Inscripto")


        # OPCIÓN 2 - Cambiar clave
        elif opcion == 2:

            # Se solicita la nueva clave
            nueva_clave = input("Nueva clave: ")

            # Se verifica que tenga como mínimo 6 caracteres
            if len(nueva_clave) < 6:

                print("Error: mínimo 6 caracteres.")

            else:

                # Se solicita nuevamente para confirmar
                confirmar_clave = input("Confirmar clave: ")

                # Se comprueba si las dos claves son iguales
                if nueva_clave == confirmar_clave:

                    # Se reemplaza la clave anterior
                    clave_correcta = nueva_clave

                    print("Clave cambiada correctamente.")

                else:

                    print("Error: las claves no coinciden.")


        # OPCIÓN 3 - Mostrar mensaje motivacional
        elif opcion == 3:

            print("Confia en ti mismo")


        # OPCIÓN 4 - Salir del sistema
        elif opcion == 4:

            print("Saliendo del sistema.")

            # Cambia a True para terminar el while
            salir = True