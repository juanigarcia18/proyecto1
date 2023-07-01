from productos import GestionProductos
from clientes import GestionClientes
import json
from datetime import datetime


class Venta:
    IVA = 0.16
    IGTF = 0.03
    def __init__(self, cliente, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2, total):
        self.cliente = cliente
        self.productos = productos
        self.cantidad = cantidad
        self.pago = pago
        self.envio = envio
        self.fecha = fecha
        self.cliente_tipo = cliente_tipo
        self.pago2 = pago2
        self.total = total
    

class GestionVentas:
    def __init__(self):
        self.ventas = []
        self.gestion_productos = GestionProductos()
        self.gestion_clientes = GestionClientes()
        self.cargar_ventas()

    
    def guardar_ventas(self):
        ventas_guardar = [vars(venta['venta']) for venta in self.ventas]
        with open('ventas.json', 'w') as f:
            json.dump(ventas_guardar, f, indent=4)

    def cargar_ventas(self):
        try:
            with open('ventas.json', 'r') as f:
                ventas_cargadas = json.load(f)
                self.ventas = [{'venta': Venta(**venta), **venta} for venta in ventas_cargadas]
        except FileNotFoundError:
            self.ventas = []

    def calcular_subtotal(self, productos, cantidad, pago, cliente_tipo, pago2):
            nombres_productos = productos.lower().split(',')  # Convert input to lowercase
            cantidades = list(map(int, cantidad.split(',')))  # Convert quantities to integers
            subtotal = 0
            for nombre_producto, cantidad in zip(nombres_productos, cantidades):
                producto_objeto = self.gestion_productos.buscar_productos(nombre=nombre_producto.strip())
                if producto_objeto:
                    precio_producto = self.gestion_productos.obtener_precio_producto(nombre_producto)
                    if precio_producto is not None:
                        subtotal += int(precio_producto) * cantidad  # Use the quantity from the list

            descuento = subtotal * 0.05 if cliente_tipo == 'juridico' and pago2 == 's' else 0
            iva = subtotal * 0.16
            igtf = subtotal * 0.03 if pago in ['zelle', 'cash'] else 0
            total = subtotal - descuento + iva + igtf

            return subtotal



    def calcular_total(self, pago, cliente_tipo, pago2, subtotal):

        descuento = subtotal * 0.05 if cliente_tipo == 'juridico' and pago2 == 's' else 0
        iva = subtotal * 0.16
        igtf = subtotal * 0.03 if pago in ['zelle', 'cash'] else 0
        total = subtotal - descuento + iva + igtf

        return total
    
    
    
    def registrar_venta(self, cliente_documento, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2, total, subtotal):
        venta = Venta(cliente_documento, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2, total)
        nombre_cliente = self.gestion_clientes.buscar_nombre_cliente_por_documento(cliente_documento)
        descuento = subtotal * 0.05 if cliente_tipo == 'juridico' and pago2 == 's' else 0
        iva = subtotal * 0.16
        igtf = subtotal * 0.03 if pago in ['zelle', 'cash'] else 0
        
        self.ventas.append({
            'venta' : venta,
            'cliente': nombre_cliente,
            'documento': cliente_documento,
            'productos': productos,
            'cantidad': cantidad,
            'pago': pago,
            'envio': envio,
            'subtotal': subtotal,
            'descuento': descuento,
            'iva': iva,
            'igtf': igtf,
            'total': total,
            'fecha': fecha
        })

        print("\nVenta registrada:\n")
        print("Cliente:", cliente_documento)
        print("Productos:", productos)
        print("Cantidad:", cantidad)
        print("Pago:", pago)
        print("Envío:", envio)
        print("Subtotal:", subtotal)
        print("Descuento:", descuento)
        print("IVA:", iva)
        print("IGTF:", igtf)
        print("Total:", total)

        return {
            'cliente': nombre_cliente,
            'documento': cliente_documento,
            'productos': productos,
            'cantidad': cantidad,
            'pago': pago,
            'envio': envio,
            'subtotal': subtotal,
            'descuento': descuento,
            'iva': iva,
            'igtf': igtf,
            'total': total
        }

    
    def buscar_venta_por_cliente(self, cliente_documento):
        for venta in self.ventas:
            if venta['venta'].cliente == cliente_documento:
                return venta
        return None
    
    def buscar_envio_por_documento(self, cliente_documento):
        for venta in self.ventas:
            if venta['venta'].cliente == cliente_documento:
                return venta['venta'].envio

        return None

    def buscar_ventas(self, cliente=None, fecha=None, total=None):
            ventas_encontradas = []
            for venta in self.ventas:
                venta_info = venta['venta']
                if (cliente is None or venta_info.cliente == cliente) and \
                (fecha is None or venta_info.fecha == fecha) and \
                (total is None or venta['total'] == total):
                    ventas_encontradas.append(venta)

            return ventas_encontradas

    def buscar_venta_por_documento(self, documento):
        with open('ventas.json', 'r') as f:
            ventas = json.load(f)

        for venta in ventas:
            if venta['cliente'] == documento:
                print("\nVenta encontrada:\n")
                print("Cliente:", venta['cliente'])
                print("Productos:", venta['productos'])
                print("Cantidad:", venta['cantidad'])
                print("Pago:", venta['pago'])
                print("Envío:", venta['envio'])
                print("Total:", venta['total'])
                return

        print("No se encontró ninguna venta con ese documento.")

        
    def buscar_ventas_por_rango_fechas(self, fecha_inicio, fecha_fin):
        with open('ventas.json', 'r') as f:
            ventas = json.load(f)

        ventas_encontradas = []
        for venta in ventas:
            fecha_venta = datetime.strptime(venta['fecha'], "%d/%m/%Y")
            fecha_inicio_rango = datetime.strptime(fecha_inicio, "%d/%m/%Y")
            fecha_fin_rango = datetime.strptime(fecha_fin, "%d/%m/%Y")

            if fecha_inicio_rango <= fecha_venta <= fecha_fin_rango:
                ventas_encontradas.append(venta)

        if len(ventas_encontradas) > 0:
            print("\nVentas encontradas:\n")
            for venta in ventas_encontradas:
                print("Venta encontrada:")
                print("Cliente:", venta['cliente'])
                print("Productos:", venta['productos'])
                print("Cantidad:", venta['cantidad'])
                print("Pago:", venta['pago'])
                print("Envío:", venta['envio'])
                print("Total:", venta['total'])
        else:
            print("No se encontraron ventas que coincidan con el rango de fechas especificado")


    def buscar_ventas_por_rango_montos(self, monto_min, monto_max):
        with open('ventas.json', 'r') as f:
            ventas = json.load(f)

        ventas_encontradas = []
        for venta in ventas:
            total_venta = venta['total']
            if monto_min <= total_venta <= monto_max:
                ventas_encontradas.append(venta)

        if len(ventas_encontradas) > 0:
            print("\nVentas encontradas:\n")
            for venta in ventas_encontradas:
                print("Venta encontrada:")
                print("Cliente:", venta['cliente'])
                print("Productos:", venta['productos'])
                print("Cantidad:", venta['cantidad'])
                print("Pago:", venta['pago'])
                print("Envío:", venta['envio'])
                print("Total:", venta['total'])
        else:
            print("No se encontraron ventas que coincidan con el rango de montos especificado")