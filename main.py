from productos import GestionProductos
from ventas import GestionVentas
from clientes import GestionClientes
from pagos import GestionPagos
from envios import GestionEnvios
from estadisticas import Estadisticas
import os
import random


def main():


    gestion_productos = GestionProductos()

    if os.path.isfile('productos.json'):
        print("El archivo productos.json ya existe\n")
        
    else:
        gestion_productos.obtener_productos_api()
        gestion_productos.guardar_productos_json()
    

    gestion_ventas = GestionVentas()
    gestion_clientes = GestionClientes()
    gestion_pagos = GestionPagos()
    gestion_envios = GestionEnvios()
    estadisticas = Estadisticas(gestion_ventas.ventas, gestion_pagos.pagos, gestion_envios.envios)

    while True:
        print("\n=====Bienvenido=====\n")
        print("1. Gestion de clientes")
        print("2. Gestion de productos")
        print("3. Gestion de ventas")
        print("4. Gestion de pagos")
        print("5. Gestion de envios")
        print("6. Estadisticas")
        print("7. Cargar condiciones iniciales")
        print("8. Salir")
        opcion = input("\nSeleccione una opcion: ")

        # Listo 

        if opcion == "1":

            while True:
                print("\n=====Gestion de clientes=====\n")
                print("1.1 Registrar cliente")
                print("1.2 Buscar cliente")
                print("1.3 Imprimir lista de clientes")
                print("1.4 Volver")
                opcion_cliente = input("\nSeleccione una opcion: ")

                # Validacion
                while opcion_cliente not in ["1.1", "1.2", "1.3", "1.4"]:
                    print("\nOpcion no valida\n\n=====Gestion de clientes=====\n\n1.1 Registrar cliente")
                    print("1.2 Buscar cliente")
                    print("1.3 Imprimir lista de clientes")
                    print("1.4 Volver")
                    opcion_cliente = input("\nSeleccione una opcion: ")   

                # Registrar un cliente
                if opcion_cliente == "1.1":
                    nombre = input("Ingrese el nombre del cliente: ")
                    tipo_cliente = input("Ingrese el tipo de cliente (natural/juridico): ")
                    
                    # Validacion
                    while tipo_cliente.lower() not in ["natural", "juridico"] :
                        print("Error, debe ser natural o juridico")
                        tipo_cliente = input("Ingrese el tipo de cliente (natural/juridico): ").lower()
                                             
                    documento = input("Ingrese su documento (cedula/rif): ").lower()
                    correo = input("Ingrese su correo: ")
                    direccion = input("Ingrese su direccion de envio:")
                    telefono = input("Ingrese su numero de telefono: ")

                    gestion_clientes.agregar_cliente(nombre, tipo_cliente, documento, correo, direccion, telefono)

                
                # Buscar cliente por documento o correo
                elif opcion_cliente == "1.2":

                    opcion2 = input("1.2.1 Buscar por documento (cedula/rif)\n1.2.2 Buscar por correo\nOpcion: ")

                    if opcion2 == "1.2.1":
                        documento = input("Ingrese el documento del cliente a buscar: ").lower()
                        clientes_encontrados = gestion_clientes.buscar_cliente(documento=documento)
                        if clientes_encontrados:
                            for cliente in clientes_encontrados:
                                print(cliente)  
                        else:
                            print("No se encontro ningun cliente con el documento proporcionado")

                    elif opcion2 == "1.2.2":
                        correo = input("Ingrese el correo del cliente a buscar: ")
                        clientes_encontrados = gestion_clientes.buscar_cliente(correo=correo)
                        if clientes_encontrados:
                            for cliente in clientes_encontrados:
                                print(cliente)  
                        else:
                            print("No se encontro ningun cliente con el correo proporcionado")
                
                # Imprimir lista de clientes en un txt
                elif opcion_cliente == "1.3":
                    
                    gestion_clientes.guardar_clientes()


                # volver al menu anterior
                elif opcion_cliente == "1.4":
                    break

       

        # Listo

        elif opcion == "2":

            while True :
                print("\n=====Gestion de Productos=====\n")
                print("2.1 Registrar producto")
                print("2.2 Buscar producto")
                print("2.3 Modificar producto")
                print("2.4 Eliminar producto")
                print("2.5 Volver")
                opcion_producto = input("\nSeleccione una opción: ")

                
                # Validacion
                while opcion_producto not in ["2.1", "2.2", "2.3", "2.4", "2.5"]:
                    print("\nOpcion no valida\n\n=====Gestion de Productos=====\n\n2.1 Registrar producto")
                    print("2.2 Buscar producto")
                    print("2.3 Modificar producto")
                    print("2.4 Eliminar producto")
                    print("2.5 Volver")
                    opcion_producto = input("\nSeleccione una opción: ")

                if opcion_producto == "2.1":
                    
                    name = input("Ingrese el nombre del producto: ")
                    description = input("Ingrese la descripción del producto: ")
                    price = float(input("Ingrese el precio del producto: "))
                    category = input("Ingrese la categoría del producto: ")
                    quantity = int(input("Ingrese la cantidad del producto: "))
                    gestion_productos.agregar_producto(name, description, price, category, quantity)
                    print("Producto registrado correctamente")

                # FALTA BUSCAR PRODUCTOS TAMBIEN POR CATEGORIA PRECIO DISPONIBILIDAD
                elif opcion_producto == "2.2":
                    # Opciones de búsqueda
                    print("Seleccione el criterio de búsqueda:")
                    print("2.2.1 Categoría")
                    print("2.2.2 Precio")
                    print("2.2.3 Nombre")
                    print("2.2.4 Disponibilidad")
                    opcion_busqueda = input("Ingrese la opción de búsqueda: ")

                    while opcion_busqueda not in ["2.2.1", "2.2.2", "2.2.3", "2.2.4"]:
                        print("Seleccione el criterio de busqueda:")
                        print("2.2.1 Categoría")
                        print("2.2.2 Precio")
                        print("2.2.3 Nombre")
                        print("2.2.4 Disponibilidad")
                        opcion_busqueda = input("Ingrese la opción de busqueda: ")

                    if opcion_busqueda == "2.2.1":
                        # Búsqueda por categoria
                        categoria = input("Ingrese la categoría del producto a buscar: ")
                        productos_encontrados = gestion_productos.buscar_productos(categoria=categoria)
                    elif opcion_busqueda == "2.2.2":
                        # Busqueda por precio
                        precio_min = float(input("Ingrese el precio mínimo: "))
                        precio_max = float(input("Ingrese el precio máximo: "))
                        productos_encontrados = gestion_productos.buscar_productos(precio_min=precio_min, precio_max=precio_max)
                    elif opcion_busqueda == "2.2.3":
                        # Búsqueda por nombre
                        nombre = input("Ingrese el nombre del producto a buscar: ")
                        productos_encontrados = gestion_productos.buscar_productos(nombre=nombre)
                    elif opcion_busqueda == "2.2.4":
                        # Búsqueda por disponibilidad
                        disponibilidad = input("Desea buscar productos disponibles? (1. Si/2. No): ")
                        disponibilidad = disponibilidad.lower() == "1"
                        productos_encontrados = gestion_productos.buscar_productos(disponibilidad=disponibilidad)
                    else:
                        print("Opción inválida")
                        continue

                    if productos_encontrados:
                        print("Productos encontrados:")
                        for producto in productos_encontrados:
                            print(producto)
                    else:
                        print("No se encontraron productos que coincidan con los criterios de búsqueda")

                        
                elif opcion_producto == "2.3":
                    nombre = input("Ingrese el nombre del producto a modificar: ")
                    
                    new_name = input("Ingrese el nuevo nombre del producto: ")
                    new_description = input("Ingrese la nueva descripción del producto: ")
                    
                    while True:
                        new_price = input("Ingrese el nuevo precio del producto: ")
                        try:
                            new_price = float(new_price)
                            break  # Salir del bucle si se ingresa un número válido
                        except ValueError:
                            print("Ingrese un número válido para el precio")
                    
                    new_category = input("Ingrese la nueva categoría del producto: ")
                    
                    while True:
                        new_quantity = input("Ingrese la nueva cantidad del producto: ")
                        try:
                            new_quantity = int(new_quantity)
                            break  # Salir del bucle si se ingresa un número válido
                        except ValueError:
                            print("Ingrese un numero valido para la cantidad")
                    
                    if gestion_productos.modificar_producto(nombre, new_name, new_description, new_price, new_category, new_quantity):
                        print("Producto modificado correctamente")
                    else:
                        print("No se pudo modificar el producto")


                        
                elif opcion_producto == "2.4":
                    nombre = input("Ingrese el nombre del producto a eliminar: ")
                    productos_encontrados = gestion_productos.buscar_productos(nombre)
                    if productos_encontrados:
                        for producto in productos_encontrados:
                            if gestion_productos.eliminar_producto(producto.name):
                                print("Producto eliminado correctamente")
                            else:
                                print("No se pudo eliminar el producto")
                    else:
                        print("No se encontro ningun producto con el nombre proporcionado")
                
                # volver al menu anterior
                elif opcion_producto == "2.5":
                    break
                

        
        # Listo  
        
        elif opcion == "3":

            while True :
                print("\n=====Gestion de Ventas=====\n")
                print("3.1 Registrar venta")
                print("3.2 Buscar venta")
                print("3.3 Volver")
                opcion_venta = input("\nSeleccione una opción: ")

                # Validacion
                while opcion_venta not in ["3.1", "3.2", "3.3"]:
                    print("\nOpcion no valida\n\n=====Gestion de Ventas=====\n\n3.1 Registrar venta")
                    print("3.2 Buscar venta")
                    print("3.3 Generar Factura")
                    print("3.4 Volver")
                    opcion_venta = input("\nSeleccione una opcion: ")

                if opcion_venta == "3.1":
                    # Registrar venta
                    documento = input("Ingrese el documento del cliente: ").lower()
                    clientes_encontrados = gestion_clientes.buscar_cliente(documento=documento)

                    if clientes_encontrados:
                        cliente = clientes_encontrados[0]  # Tomar el primer cliente encontrado
                        cliente_tipo = cliente.tipo_cliente
                        cliente_documento = cliente.documento

                        fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
                        productos = input("Ingrese el/los productos comprados separado por comas: ")
                        cantidad = input("Ingrese la cantidad de cada uno separado por comas: ")
                        print("Metodos de pago disponibles: Zelle, Cash, PM, PdV")
                        pago = input("Ingrese su método de pago: ").lower()
                        pago2 = input("Ingrese si pagó de contado (s/n): ").lower()
                        print("Métodos de envío disponibles: MRW, Zoom, Delivery")
                        envio = input("Ingrese su método de envío: ")
                        
                        subtotal = gestion_ventas.calcular_subtotal(productos, cantidad, pago, cliente_tipo, pago2)
                        total = gestion_ventas.calcular_total(pago, cliente_tipo, pago2, subtotal)
                        gestion_ventas.registrar_venta(cliente_documento, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2, total, subtotal)
                        gestion_ventas.guardar_ventas()
                        print("Venta registrada con éxito")
                    else:
                        print("No se encontro ningun cliente con el documento proporcionado")
                        continue
            
                # revisar
                elif opcion_venta == "3.2":
                    # Opciones de búsqueda
                    print("Seleccione el criterio de búsqueda:")
                    print("3.2.1 Cliente")
                    print("3.2.2 Fecha")
                    print("3.2.3 Monto")
                    opcion_busqueda = input("Ingrese la opción de búsqueda: ")

                    if opcion_busqueda == "3.2.1":
                        # Búsqueda por cliente
                        documento = input("Ingrese el documento del cliente a buscar: ")
                        gestion_ventas.buscar_venta_por_documento(documento)
                    elif opcion_busqueda == "3.2.2":
                        # Búsqueda por fecha
                        fecha_inicio = input("Ingrese la fecha de inicio del rango (dd/mm/aaaa): ")
                        fecha_fin = input("Ingrese la fecha de fin del rango (dd/mm/aaaa): ")
                        gestion_ventas.buscar_ventas_por_rango_fechas(fecha_inicio, fecha_fin)

                    elif opcion_busqueda == "3.2.3":
                        # Búsqueda por monto
                        monto_min = float(input("Ingrese el monto mínimo de la venta a buscar: "))
                        monto_max = float(input("Ingrese el monto maximo de la venta a buscar: "))
                        gestion_ventas.buscar_ventas_por_rango_montos(monto_min, monto_max)

                    else:
                        print("Opción invalida")
                        continue

                # volver al menu
                elif opcion_venta == "3.3":
                    break


        # Lista      


        elif opcion == "4":

            while True :
                print("\n=====Gestion de Pagos=====\n")
                print("4.1 Registrar pago")
                print("4.2 Buscar pago")
                print("4.3 Volver")
                opcion_pago = input("\nSeleccione una opción: ")
                
                # Validacion
                while opcion_pago not in ["4.1", "4.2", "4.3"]:
                    print("\nOpcion no valida\n\n=====Gestion de Pagos=====\n")
                    print("4.1 Registrar pago")
                    print("4.2 Buscar pago")
                    print("4.3 Volver")
                    opcion_pago = input("\nSeleccione una opcion: ")
                    
                if opcion_pago == "4.1":
                    cliente_documento = input("Ingrese el documento del cliente: ").lower()
                    cliente = gestion_ventas.buscar_venta_por_cliente(cliente_documento)
                    cliente = cliente['cliente'] # devuelve el documento relacionado a la venta
                    
                    monto = gestion_ventas.buscar_venta_por_cliente(cliente_documento)
                    monto = monto['total'] # devuelve el total de la venta
                    
                    moneda = gestion_ventas.buscar_venta_por_cliente(cliente_documento)
                    moneda = moneda['pago']
                    if moneda in ["zelle", "cash"] :
                        moneda = "dolar"
                    else :
                        moneda = "bolivares"
                    tipo = gestion_ventas.buscar_venta_por_cliente(cliente_documento)
                    tipo = tipo['pago']
                    fecha = input("Ingrese la fecha del pago (dd/mm/aaaa): ")
                    gestion_pagos.registrar_pago(cliente, monto, moneda, tipo, fecha)
            
                elif opcion_pago == "4.2":

                    opcion2 = input("\n4.2.1 Buscar por cliente\n4.2.2 Buscar por fecha\n4.2.3 Buscar por tipo de pago\n4.2.4 Buscar por moneda de pago\nSeleccione una opcion: ")

                    while opcion2 not in ["4.2.1", "4.2.2", "4.2.3", "4.2.4"]:
                        opcion2 = input("\n4.2.1 Buscar por cliente\n4.2.2 Buscar por fecha\n4.2.3 Buscar por tipo de pago\n4.2.4 Buscar por moneda de pago\nSeleccione una opcion valida: ")

                    if opcion2 == "4.2.1":
                        cliente_nombre = input("Ingrese el documento del cliente: ")
                        pagos_encontrados = gestion_pagos.buscar_pago(cliente=cliente_nombre)
                        if pagos_encontrados:
                            for pago in pagos_encontrados:
                                print(pago)
                        else:
                            print("No se encontraron pagos para el cliente especificado")

                    elif opcion2 == "4.2.2":
                        fecha_pago = input("Ingrese la fecha del pago (dd/mm/aaaa):  ")
                        pagos_encontrados = gestion_pagos.buscar_pago(fecha=fecha_pago)
                        if pagos_encontrados:
                            for pago in pagos_encontrados:
                                print(pago)
                        else:
                            print("No se encontraron pagos para la fecha especificada")

                    elif opcion2 == "4.2.3":
                        tipo_pago = input("Ingrese el tipo de pago: ")
                        pagos_encontrados = gestion_pagos.buscar_pago(tipo=tipo_pago)
                        if pagos_encontrados:
                            for pago in pagos_encontrados:
                                print(pago)
                        else:
                            print("No se encontraron pagos para el tipo de pago especificado")

                    elif opcion2 == "4.2.4":
                        moneda_pago = input("Ingrese la moneda del pago: ")
                        pagos_encontrados = gestion_pagos.buscar_pago(moneda=moneda_pago)
                        if pagos_encontrados:
                            for pago in pagos_encontrados:
                                print(pago)
                        else:
                            print("No se encontraron pagos para la moneda especificada")
                    
                # volver al menu
                elif opcion_pago == "4.3":
                    break
        
        # Listo todo
        elif opcion == "5":

            while True:
                print("\n=====Gestion de Envios=====\n")
                print("5.1 Registrar envio")
                print("5.2 Buscar envio")
                print("5.3 Volver")
                opcion_envio = input("\nSeleccione una opción: ")

                # Validación
                while opcion_envio not in ["5.1", "5.2", "5.3"]:
                    print("\nOpcion no valida\n\n=====Gestion de Envios=====\n")
                    print("5.1 Registrar envio")
                    print("5.2 Buscar envio")
                    print("5.3 Volver")
                    opcion_envio = input("\nSeleccione una opcion: ")

                if opcion_envio == "5.1":
                    cliente_documento = input("Ingrese el documento del cliente: ").lower()
                    cliente = gestion_ventas.buscar_venta_por_cliente(cliente_documento)
                    cliente = cliente['cliente']

                    if cliente is None:
                        print("No se encontro un registro de venta asociado al cliente")
                    
                    direccion = gestion_clientes.buscar_direccion_por_documento(cliente_documento)

                    order_compra = str(random.randint(1000, 9999))
                    servicio = gestion_ventas.buscar_envio_por_documento(cliente_documento)

                    if servicio == "delivery":
                        motorizado = input("Ingrese los datos del motorizado (nombre, teléfono): ")
                    else :
                        motorizado = None

                    costo = float(5 * random.randint(1, 4))
                    # REVISAR
                    fecha = input("Ingrese la fecha del envío (dd/mm/aaaa): ")

                    gestion_envios.registrar_envio(cliente, order_compra, servicio, costo, direccion, motorizado, fecha)
                    print("Envío registrado exitosamente")


                elif opcion_envio == "5.2":
                    opcion_envio2 = input("\n5.2.1 Buscar por cliente\n5.2.2 Buscar por fecha\nSeleccione una opcion: ")

                    while opcion_envio2 not in ["5.2.1", "5.2.2"]:
                        opcion_envio2 = input("\nOpcion invalida.\n\n5.2.1 Buscar por cliente\n5.2.2 Buscar por fecha\nSeleccione una opcion valida: ")

                    if opcion_envio2 == "5.2.1":
                        cliente = input("Ingrese el documento del cliente a buscar: ")
                        envios = gestion_envios.buscar_envios(cliente)

                        if envios:
                            print("Envios encontrados:")
                            for envio in envios:
                                print(envio)
                        else:
                            print("No se encontraron envios")

                    elif opcion_envio2 == "5.2.2":
                        fecha = input("Ingrese la fecha (dd/mm/aaaa) a buscar: ")
                        envios = gestion_envios.buscar_envios(fecha=fecha)

                        if envios:
                            print("Envios encontrados:")
                            for envio in envios:
                                print(envio)
                        else:
                            print("No se encontraron envios")


                # Volver al menu
                elif opcion_envio == "5.3":
                    break

        
        # REVISAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR
        elif opcion == "6":

            while True :
                print("\n=====Estadisticas=====\n")
                print("6.1 Generar informe de ventas")
                print("6.2 Generar informe de pagos")
                print("6.3 Generar informe de envios")
                print("6.4 Volver")
                opcion_informe = input("\nSeleccione una opcion: ")

                # Validacion
                while opcion_informe not in ["6.1", "6.2", "6.3", "6.4"]:
                    print("Opcion no valida\n\n=====Estadisticas=====\n")
                    print("6.1 Generar informe de ventas")
                    print("6.2 Generar informe de pagos")
                    print("6.3 Generar informe de envios")
                    print("6.4 Volver")
                    opcion_informe = input("\nSeleccione una opcion: ")


                if opcion_informe == "6.1":
                    estadisticas.generar_informe_ventas()
                elif opcion_informe == "6.2":
                    estadisticas.generar_informe_pagos()
                elif opcion_informe == "6.3":
                    estadisticas.generar_informe_envios()
                
                # volver al menu
                elif opcion_informe == "6.4":
                    break
        
        
        # TERMINAR DE AGREGAR LO DEMAS
        elif opcion == "7":
            if os.path.isfile('productos.json'):
                os.remove('productos.json')
                os.remove('clientes.json')
                os.remove('envios.json')
                os.remove('ventas.json')
                os.remove('pagos.json')
                gestion_productos.productos.clear()
                gestion_clientes.clientes.clear()
                gestion_envios.envios.clear()
                gestion_ventas.ventas.clear()
                gestion_pagos.pagos.clear()
                gestion_productos.obtener_productos_api()
                gestion_productos.guardar_productos_json()

        elif opcion == "8":
            break    


        else:
            
            print("\nOpcion no valida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
