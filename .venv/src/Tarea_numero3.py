from functools import reduce

# Inventario inicial
inventario = [
    {'id': 1, 'nombre': 'Manzana', 'precio': 1.0, 'cantidad': 50},
    {'id': 2, 'nombre': 'Banana', 'precio': 0.5, 'cantidad': 100},
    {'id': 3, 'nombre': 'Naranja', 'precio': 0.75, 'cantidad': 80},
    {'id': 4, 'nombre': 'Pera', 'precio': 1.25, 'cantidad': 60},
    {'id': 5, 'nombre': 'Uva', 'precio': 2.0, 'cantidad': 30},
    {'id': 6, 'nombre': 'Melón', 'precio': 3.5, 'cantidad': 20},
    {'id': 7, 'nombre': 'Sandía', 'precio': 4.0, 'cantidad': 15},
    {'id': 8, 'nombre': 'Durazno', 'precio': 2.5, 'cantidad': 25},
    {'id': 9, 'nombre': 'Fresa', 'precio': 1.75, 'cantidad': 40},
    {'id': 10, 'nombre': 'Kiwi', 'precio': 2.25, 'cantidad': 35}
]

# Registro de ventas (lista vacía)
registro_ventas = []

# Consultar producto por ID
def consultar_producto(inventario, id_producto):
    return next(filter(lambda producto: producto['id'] == id_producto, inventario), None)

# Actualizar un producto existente
def actualizar_producto(inventario, id_producto, nuevo_nombre, nuevo_precio, nueva_cantidad):
    return list(map(
        lambda producto: {'id': id_producto, 'nombre': nuevo_nombre, 'precio': nuevo_precio, 'cantidad': nueva_cantidad}
        if producto['id'] == id_producto else producto,
        inventario))

# Registrar un nuevo producto
def registrar_nuevo_producto(inventario, nombre, precio, cantidad):
    nuevo_id = max(map(lambda p: p['id'], inventario)) + 1  # Generar nuevo ID
    nuevo_producto = {'id': nuevo_id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    return inventario + [nuevo_producto]

# Registrar venta (actualizar inventario)
def actualizar_inventario(inventario, ventas):
    for venta in ventas:
        inventario = registrar_venta(inventario, venta['id'], venta['cantidad'])
    return inventario

# Registrar venta (descontar producto)
def registrar_venta(inventario, id_producto, cantidad_vendida):
    return list(map(
        lambda producto: {**producto, 'cantidad': producto['cantidad'] - cantidad_vendida}
        if producto['id'] == id_producto and producto['cantidad'] >= cantidad_vendida else producto,
        inventario
    ))

# Totalizar compra
def totalizar_compra(inventario, ventas):
    return reduce(
        lambda total, venta: total + (consultar_producto(inventario, venta['id'])['precio'] * venta['cantidad']
                                      if consultar_producto(inventario, venta['id']) else 0),
        ventas,
        0
    )

# Consulta de información general (listar todos los productos)
def consultar_inventario(inventario):
    return list(map(lambda producto: producto, inventario))

# Validar entrada de datos
def validar_entrada(prompt, tipo_dato):
    while True:
        entrada = input(prompt)
        try:
            return tipo_dato(entrada)
        except ValueError:
            print(f"Entrada inválida. Por favor ingrese un {tipo_dato.__name__} válido.")

# Menú de ventas
def menu_ventas():
    ventas = []
    global inventario

    while True:
        print()
        print("\n--- Menú de Ventas ---")
        print()
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Editar producto")
        print("4. Finalizar venta")
        print("5. Mostrar productos registrados para la venta")
        print()
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            id_producto = validar_entrada("Ingrese el ID del producto: ", int)
            producto = consultar_producto(inventario, id_producto)
            if producto:
                cantidad = validar_entrada(f"Ingrese la cantidad del producto '{producto['nombre']}' a agregar: ", int)
                if cantidad <= producto['cantidad']:
                    ventas.append({'id': id_producto, 'nombre': producto['nombre'], 'cantidad': cantidad})
                    print(f"Producto '{producto['nombre']}' agregado a la venta.")
                else:
                    print("Cantidad no disponible en inventario.")
            else:
                print("Producto no encontrado.")
                
        elif opcion == "2":
            id_producto = validar_entrada("Ingrese el ID del producto a eliminar: ", int)
            ventas = list(filter(lambda venta: venta['id'] != id_producto, ventas))
            print("Producto eliminado de la venta.")
            
        elif opcion == "3":
            id_producto = validar_entrada("Ingrese el ID del producto a editar: ", int)
            producto = next((venta for venta in ventas if venta['id'] == id_producto), None)
            if producto:
                nueva_cantidad = validar_entrada(f"Ingrese la nueva cantidad para el producto '{producto['nombre']}': ", int)
                if nueva_cantidad <= consultar_producto(inventario, id_producto)['cantidad']:
                    producto['cantidad'] = nueva_cantidad
                    print("Cantidad actualizada.")
                else:
                    print("Cantidad no disponible en inventario.")
            else:
                print("Producto no encontrado en la venta.")
                
        elif opcion == "4":
            if ventas:
                total = totalizar_compra(inventario, ventas)
                print("\n--- Resumen de la Venta ---")
                for venta in ventas:
                    print(f"Producto: {venta['nombre']}, id: {venta["id"]}, Cantidad: {venta['cantidad']}")
                print(f"Total de la venta: ${total:.2f}")
                
                # Registrar la venta en el inventario y el registro de ventas
                inventario = actualizar_inventario(inventario, ventas)
                registro_ventas.append(ventas)
                
                print("Venta finalizada.")
                break
            else:
                print("No hay productos en la venta.")

        elif opcion == "5":
            if not ventas:
                print()
                print("Aun no se han registrado productos")
                print()
                return
            else:
                total = totalizar_compra(inventario, ventas)
                print()
                print("\n--- Resumen de la Venta ---")
                print()
                for venta in ventas:
                    print(f"Producto: {venta['nombre']}, id: {venta["id"]}, Cantidad: {venta['cantidad']}")
                print(f"Total de la venta: ${total:.2f}")
        else:
            print("Opción no válida, intente de nuevo.")

# Menú principal
def menu():
    global inventario
    
    while True:
        print()
        print("\n--- Menú de la Registradora de Ventas ---")
        print()
        print("1. Consultar un producto por ID")
        print("2. Actualizar un producto existente")
        print("3. Registrar un nuevo producto")
        print("4. Registrar una venta")
        print("5. Consultar todo el inventario")
        print("6. Consultar registro de ventas")
        print("7. Salir")
        print()
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            id_producto = validar_entrada("Ingrese el ID del producto: ", int)
            producto = consultar_producto(inventario, id_producto)
            if producto:
                print(f"Producto encontrado: {producto}")
            else:
                print("Producto no encontrado.")
                
        elif opcion == "2":
            id_producto = validar_entrada("Ingrese el ID del producto a actualizar: ", int)
            nombre = input("Ingrese el nuevo nombre del producto: ")
            precio = validar_entrada("Ingrese el nuevo precio del producto: ", float)
            cantidad = validar_entrada("Ingrese la nueva cantidad del producto: ", int)
            if consultar_producto(inventario, id_producto):
                inventario = actualizar_producto(inventario, id_producto, nombre, precio, cantidad)
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")
            
        elif opcion == "3":
            nombre = input("Ingrese el nombre del nuevo producto: ")
            precio = validar_entrada("Ingrese el precio del nuevo producto: ", float)
            cantidad = validar_entrada("Ingrese la cantidad del nuevo producto: ", int)
            inventario = registrar_nuevo_producto(inventario, nombre, precio, cantidad)
            print("Nuevo producto registrado.")
            
        elif opcion == "4":
            menu_ventas()
            
        elif opcion == "5":
            print()
            print("Inventario completo:")
            print()
            for producto in consultar_inventario(inventario):
                print(producto)
                
        elif opcion == "6":
            print()
            print("Registro de ventas:")
            print()
            if registro_ventas:
                for i, venta in enumerate(registro_ventas, 1):
                    print(f"\n--- Venta {i} ---")
                    for producto in venta:
                        print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}")
                        total_venta = totalizar_compra(inventario, venta)
                        print(f"Total de la venta: ${total_venta:.2f}")
            else:
                print("No hay ventas registradas.")

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú principal
menu()