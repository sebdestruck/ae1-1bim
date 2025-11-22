# Inicio

# Sistema de facturación para librería

# preguntamos cuántas ventas deseamos registrar
n = int(input("¿Cuántas ventas desea registrar?: "))

# declaración de arreglos
nombres = []
apellidos = []
cantidads = []
precios = []
subtotals = []
descuentos = []
totales = []

# REGISTRO DE CLIENTES
for i in range(n):
    print(f"\n--- Registro de cliente {i + 1} ---")

    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    cantidad = int(input("Ingrese la cantidad de libros: "))
    precio = float(input("Ingrese el precio unitario: "))

    # calcular el subtotal
    Subtotal = precio * cantidad

    # determinar el descuento correspondiente
    es_1_libro = (cantidad == 1)
    es_2_3_libros = (cantidad >= 2 and cantidad <= 3)
    es_4_5_libros = (cantidad >= 4 and cantidad <= 5)
    es_6_o_mas = (cantidad >= 6)

    descuento = 0.0  # inicial

    if es_1_libro:
        descuento = 0.05

    if es_2_3_libros:
        descuento = 0.10

    if es_4_5_libros:
        descuento = 0.30

    if es_6_o_mas:
        descuento = 0.40

    monto_descuento = descuento * Subtotal
    total = Subtotal - monto_descuento

    # Guardar los valores en los arreglos
    nombres.append(nombre)
    apellidos.append(apellido)
    cantidads.append(cantidad)
    precios.append(precio)
    subtotals.append(Subtotal)
    descuentos.append(monto_descuento)
    totales.append(total)

# Mostrar la información de cada cliente
for i in range(n):
    print(f"\nCliente {i + 1}:")
    print("Nombre:", nombres[i])
    print("Apellido:", apellidos[i])
    print("Cantidad de libros:", cantidads[i])
    print("Precio unitario:", precios[i])
    print("Subtotal:", subtotals[i])
    print("Monto de descuento:", descuentos[i])
    print("Total a pagar:", totales[i])

# Calcular el promedio
promedio = sum(totales) / n
print("\nPromedio de ventas:", promedio)

# Obtener venta mayor y venta menor (sin max/min)
venta_alta = totales[0]
venta_baja = totales[0]

for venta in totales:
    if venta > venta_alta:
        venta_alta = venta
    if venta < venta_baja:
        venta_baja = venta

# Mostrar resultados
print("Venta más alta: $" + str(round(venta_alta, 2)))
print("Venta más baja: $" + str(round(venta_baja, 2)))

# FIN