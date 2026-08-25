# EJERCICIO 1 - CAJA DEL KIOSCO

# Se solicita el nombre del cliente
nombre = input("Cliente: ")

# Se valida que el nombre contenga solamente letras
while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Cliente: ")


# Se solicita la cantidad de productos
cantidad = input("Cantidad de productos: ")

# Se valida que la cantidad sea un número entero mayor que cero
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: la cantidad debe ser un número entero positivo.")
    cantidad = input("Cantidad de productos: ")

# Se convierte la cantidad de texto a número entero
cantidad = int(cantidad)


# Se inicializan los acumuladores de los totales
total_sin_descuento = 0
total_con_descuento = 0


# Se recorren todos los productos ingresados por el cliente
for i in range(1, cantidad + 1):

    # Se solicita el precio de cada producto
    precio = input(f"Producto {i} - Precio: ")

    # Se valida que el precio sea un número entero
    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(f"Producto {i} - Precio: ")

    # Se convierte el precio de texto a número entero
    precio = int(precio)


    # Se pregunta si el producto tiene descuento
    descuento = input("Descuento (S/N): ").lower()

    # Se valida que la respuesta sea solamente S o N
    while descuento not in ["s", "n"]:
        print("Error: debe ingresar S o N.")
        descuento = input("Descuento (S/N): ").lower()


    # Se acumula el precio original del producto
    total_sin_descuento += precio


    # Si tiene descuento, se aplica un 10%
    if descuento == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio


    # Se acumula el precio final del producto
    total_con_descuento += precio_final


# Se calcula cuánto dinero se ahorró por los descuentos
ahorro = total_sin_descuento - total_con_descuento

# Se calcula el promedio pagado por producto
promedio = total_con_descuento / cantidad


# Se muestran los resultados finales
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
    
