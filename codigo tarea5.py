# ---------------------------------------------------------
# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación
# Evaluación Final - Problema 3
# Auditoría de Inventario
# ---------------------------------------------------------

# Función para calcular la cantidad que se debe solicitar
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


# Matriz para almacenar el inventario
inventario = []

print("=" * 55)
print("         SISTEMA DE AUDITORÍA DE INVENTARIO")
print("=" * 55)

cantidad_articulos = 5

# Registro de los artículos
for i in range(cantidad_articulos):

    print(f"\nRegistro del artículo {i + 1}")

    codigo = input("Código: ")
    nombre = input("Nombre del artículo: ")
    stock_actual = int(input("Stock actual: "))
    stock_minimo = int(input("Stock mínimo: "))

    inventario.append([codigo, nombre, stock_actual, stock_minimo])

print("\n" + "=" * 55)
print("          REPORTE DE REABASTECIMIENTO")
print("=" * 55)

articulos_reabastecer = 0
total_unidades = 0

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_pedido(stock_actual, stock_minimo)

    if cantidad > 0:
        estado = "Reabastecer"
        articulos_reabastecer += 1
        total_unidades += cantidad
    else:
        estado = "Stock suficiente"

    print("\n---------------------------------------")
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a solicitar:", cantidad)
    print("Estado:", estado)

print("\n=======================================")
print("RESUMEN GENERAL")
print("=======================================")
print("Artículos que necesitan reabastecimiento:", articulos_reabastecer)
print("Total de unidades a solicitar:", total_unidades)
print("=======================================")
print("Programa finalizado.")