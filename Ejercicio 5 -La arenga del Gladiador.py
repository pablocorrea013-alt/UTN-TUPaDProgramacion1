# EJERCICIO 5 - LA ARENA DEL GLADIADOR

print("--- BIENVENIDO A LA ARENA ---")

# nombre del jugador
nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")


# datos iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
danio_enemigo = 12

turno_gladiador = True
juego_activo = True


print("=== INICIO DEL COMBATE ===")


# el juego continúa mientras los dos tengan vida
while vida_jugador > 0 and vida_enemigo > 0 and juego_activo == True:

    # turno del jugador
    if turno_gladiador == True:

        print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")


        # validar que sea un número
        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)


        # validar que esté entre 1 y 3
        while opcion < 1 or opcion > 3:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ")

            opcion = int(opcion)


        # ataque pesado
        if opcion == 1:

            danio = 15.0

            if vida_enemigo < 20:
                danio = ataque_pesado * 1.5
                print("¡Golpe Crítico!")

            vida_enemigo -= danio

            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")


        # rafaga veloz
        elif opcion == 2:

            print(">> ¡Inicias una ráfaga de golpes!")

            for golpe in range(3):

                vida_enemigo -= 5

                print("> Golpe conectado por 5 de daño")


        # curar
        elif opcion == 3:

            if pociones > 0:

                vida_jugador += 30
                pociones -= 1

                print("¡Usaste una poción!")
                print("Recuperaste 30 puntos de vida.")

            else:

                print("¡No quedan pociones!")


        # si el enemigo sigue vivo, le toca atacar
        if vida_enemigo > 0:
            turno_gladiador = False


    # turno del enemigo
    else:

        vida_jugador -= danio_enemigo

        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

        turno_gladiador = True


        if vida_jugador > 0 and vida_enemigo > 0:
            print("=== NUEVO TURNO ===")


# termina el juego
juego_activo = False


if vida_jugador > 0:

    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")

else:

    print("DERROTA. Has caído en combate.")