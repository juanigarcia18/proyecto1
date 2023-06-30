from productos import GestionProductos
from clientes import GestionClientes
import json

class Venta:
    IVA = 0.16
    IGTF = 0.03
    def __init__(self, cliente, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2):
        self.cliente = cliente
        self.productos = productos
        self.cantidad = cantidad
        self.pago = pago
        self.envio = envio
        self.fecha = fecha
        self.cliente_tipo = cliente_tipo
        self.pago2 = pago2
    

class GestionVentas:
    def __init__(self):
        self.ventas = []
        self.gestion_productos = GestionProductos()
        self.gestion_clientes = GestionClientes()
        self.cargar_ventas()

    # Arreglar el print 
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

    def registrar_venta(self, cliente_documento, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2):
        venta = Venta(cliente_documento, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2)
        nombre_cliente = self.gestion_clientes.buscar_nombre_cliente_por_documento(cliente_documento)
        nombres_productos = productos.split(',')
        subtotal = 0
        for nombre_producto in nombres_productos:
            producto_objeto = self.gestion_productos.buscar_producto(name=nombre_producto.strip())
            if producto_objeto:
                precio_producto = self.gestion_productos.obtener_precio_producto(nombre_producto)
                if precio_producto is not None:
                    subtotal += int(precio_producto) * int(cantidad)

        descuento = subtotal * 0.05 if cliente_tipo == 'juridico' and pago2 == 's' else 0
        iva = subtotal * 0.16
        igtf = subtotal * 0.03 if pago in ['zelle', 'cash'] else 0
        total = subtotal - descuento + iva + igtf
        self.ventas.append({
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
        print("Cliente:", nombre_cliente + ", documento:", cliente_documento)
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

    # ARREGLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR
    def buscar_ventas(self, cliente=None, fecha=None, total=None):
        ventas_encontradas = []
        for venta in self.ventas:
            venta_info = venta['venta']
            if (cliente is None or venta_info.cliente == cliente) and \
               (fecha is None or venta_info.fecha == fecha) and \
               (total is None or venta['total'] == total):
                ventas_encontradas.append(venta)

        return ventas_encontradas
    
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
