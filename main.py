from productos import GestionProductos
from ventas import GestionVentas
from clientes import GestionClientes
from pagos import GestionPagos
from envios import GestionEnvios
from estadisticas import Estadisticas
import os


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
                        tipo_cliente = input("Ingrese el tipo de cliente (natural/juridico): ")
                                             
                    documento = input("Ingrese su documento (cedula/rif): ")
                    correo = input("Ingrese su correo: ")
                    direccion = input("Ingrese su direccion de envio:")
                    telefono = input("Ingrese su numero de telefono: ")

                    gestion_clientes.agregar_cliente(nombre, tipo_cliente, documento, correo, direccion, telefono)

                
                # Buscar cliente por documento o correo
                elif opcion_cliente == "1.2":

                    opcion2 = input("1.2.1 Buscar por documento (cedula/rif)\n1.2.2 Buscar por correo\nOpcion: ")

                    if opcion2 == "1.2.1":
                        documento = input("Ingrese el documento del cliente a buscar: ")
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
                            print("No se encontró ningun cliente con el correo proporcionado")
                
                # Imprimir lista de clientes en un txt
                elif opcion_cliente == "1.3":
                    
                    gestion_clientes.guardar_clientes_txt()


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
                    nombre = input("Ingrese el nombre del producto a buscar: ")
                    productos_encontrados = gestion_productos.buscar_producto(name=nombre)
                    if productos_encontrados:
                        for producto in productos_encontrados:
                            print(producto)
                    else:
                        print("No se encontro ningun producto con el nombre proporcionado")
                        
                elif opcion_producto == "2.3":
                    nombre = input("Ingrese el nombre del producto a modificar: ")
                    productos_encontrados = gestion_productos.buscar_producto(name=nombre)
                    
                    if productos_encontrados:
                        new_name = input("Ingrese el nuevo nombre del producto: ")
                        new_description = input("Ingrese la nueva descripción del producto: ")
                        
                        while True:
                            new_price = input("Ingrese el nuevo precio del producto: ")
                            try:
                                new_price = float(new_price)
                                break  # Salir del bucle si se ingresa un numero valido
                            except ValueError:
                                print("Ingrese un numero valido para el precio")
                        
                        new_category = input("Ingrese la nueva categoría del producto: ")
                        
                        while True:
                            new_quantity = input("Ingrese la nueva cantidad del producto: ")
                            try:
                                new_quantity = int(new_quantity)
                                break  # Salir del bucle si se ingresa un numero valido
                            except ValueError:
                                print("Ingrese un numero valido para la cantidad")
                        
                        for producto in productos_encontrados:
                            if gestion_productos.modificar_producto(producto.name, new_name, new_description, new_price, new_category, new_quantity):
                                print("Producto modificado correctamente")
                            else:
                                print("No se pudo modificar el producto")
                    else:
                        print("No se encontro ningun producto con el nombre proporcionado")

                        
                elif opcion_producto == "2.4":
                    nombre = input("Ingrese el nombre del producto a eliminar: ")
                    productos_encontrados = gestion_productos.buscar_producto(name=nombre)
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
                

        
      # REVISAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR  
        
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
                    print("3.3 Volver")
                    opcion_venta = input("\nSeleccione una opcion: ")

                if opcion_venta == "3.1":
                    # Registrar venta
                    cliente = input("Ingrese el nombre del cliente: ")
                    cliente_tipo = input("Ingrese si el cliente es natural o juridico: ").lower()
                    fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
                    productos = input("Ingrese el/los productos comprados separado por comas: ")
                    cantidad = input("Ingrese la cantidad: ")
                    print("metodos de pago disponibles: Zelle, Cash, PM, PdV")
                    pago = input("Ingrese su metodo de pago: ").lower() # Método de pago
                    pago2 = input("Ingrese si pago de contado (s/n)").lower()
                    print("metodos de envio disponibles: MRW, Zoom, Delivery")
                    envio = input("Ingrese su metodo de envio: ")  # Método de envío

                    gestion_ventas.registrar_venta(cliente, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2)
                    print("Venta registrada con exito")
            
            
                elif opcion_venta == "3.2":
                    # Buscar venta
                    cliente = input("Ingrese el nombre del cliente a buscar: ")
                    ventas_encontradas = gestion_ventas.buscar_ventas(cliente=cliente)

                    if len(ventas_encontradas) > 0:
                        print("Ventas encontradas:")
                        for venta in ventas_encontradas:
                            print(f"Cliente: {venta.cliente}")
                            print("Productos:")
                            for producto, cantidad in zip(venta.productos, venta.cantidad):
                                print(f"  - Nombre: {producto.name}")
                                print(f"    Descripción: {producto.description}")
                                print(f"    Precio: {producto.price}")
                                print(f"    Cantidad: {cantidad}")
                            print(f"Monto total: {venta.get_monto_total()}")
                            print("------------------------")
                
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
                    cliente = input("Ingrese el nombre del cliente: ")
                    monto = input("Ingrese el monto del pago: ")
                    moneda = input("Ingrese la moneda con la que pago: ")
                    tipo = input("Ingrese el tipo de pago (PdV, PM, Zelle, Cash): ")
                    fecha = input("Ingrese la fecha del pago (dd/mm/aaaa): ")
                    gestion_pagos.registrar_pago(cliente, monto, moneda, tipo, fecha)
            
                elif opcion_pago == "4.2":

                    opcion2 = input("\n4.2.1 Buscar por cliente\n4.2.2 Buscar por fecha\n4.2.3 Buscar por tipo de pago\n4.2.4 Buscar por moneda de pago\nSeleccione una opcion: ")

                    while opcion2 not in ["4.2.1", "4.2.2", "4.2.3", "4.2.4"]:
                        opcion2 = input("\n4.2.1 Buscar por cliente\n4.2.2 Buscar por fecha\n4.2.3 Buscar por tipo de pago\n4.2.4 Buscar por moneda de pago\nSeleccione una opcion valida: ")

                    if opcion2 == "4.2.1":
                        cliente_nombre = input("Ingrese el nombre del cliente: ")
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
        
        # Listo
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
                    cliente = input("Ingrese el nombre del cliente: ").lower()
                    while not all(char.isalpha() or char.isspace() for char in cliente):
                        cliente = input("Error\nIngrese el nombre del cliente: ").lower()
                    order_compra = input("Ingrese el numero de orden de compra: ")
                    while not order_compra.isnumeric() :
                        order_compra = input("Error\nIngrese el numero de orden de compra: ")
                    servicio = input("Ingrese el servicio de envio (MRW, Zoom, Delivery) : ").lower()
                    while not servicio in ["mrw", "zoom", "delivery"] :
                        servicio = input("Error\nIngrese el servicio de envio (MRW, Zoom, Delivery) : ").lower()
                    if servicio.lower() == "delivery" :
                        motorizado = input("Ingrese los datos del motorizado (nombre,telefono) :")
                    
                    direccion = input("Ingrese su direccion: ")
                    costo = float(input("Ingrese el costo del servicio: "))
                    fecha = input("Ingrese la fecha del envio (dd/mm/aaaa): ")

                    gestion_envios.registrar_envio(cliente, order_compra, servicio, costo, direccion, motorizado, fecha)
                    print("Envio registrado exitosamente")

                elif opcion_envio == "5.2":
                    opcion_envio2 = input("\n5.2.1 Buscar por cliente\n5.2.2 Buscar por fecha\nSeleccione una opcion: ")

                    while opcion_envio2 not in ["5.2.1", "5.2.2"]:
                        opcion_envio2 = input("\nOpcion invalida.\n\n5.2.1 Buscar por cliente\n5.2.2 Buscar por fecha\nSeleccione una opcion valida: ")

                    if opcion_envio2 == "5.2.1":
                        cliente = input("Ingrese el nombre del cliente a buscar: ")
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
                os.remove('clientes.txt')
                os.remove('envios.json')
                gestion_productos.productos.clear()
                gestion_envios.envios.clear()
                gestion_productos.obtener_productos_api()
                gestion_productos.guardar_productos_json()

        elif opcion == "8":
            break    


        else:
            
            print("\nOpcion no valida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
