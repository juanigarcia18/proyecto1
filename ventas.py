from productos import GestionProductos


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

    # REVISAR ESTOOOOOO NO PONER ID y no se si esto hace falta
    def guardar_ventas_txt(self):
        with open('ventas.txt', 'w') as f:
            for venta in self.ventas:
                f.write(f'{venta.id},{venta.cliente.id},{[producto.id for producto in venta.productos]}\n')
                        
    def registrar_venta(self, cliente, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2):
        venta = Venta(cliente, productos, cantidad, pago, envio, fecha, cliente_tipo, pago2)
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
            'venta': venta,
            'subtotal': subtotal,
            'descuento': descuento,
            'iva': iva,
            'igtf': igtf,
            'total': total,
            'fecha': fecha
        })

        print("Venta registrada:")
        print("Cliente:", cliente)
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
            'cliente': cliente,
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



    # QUITAR
    def get_monto_total(self):
        total = 0
        for producto, cantidad in zip(self.productos, self.cantidad):
            total += producto.price * cantidad
        return total
    

    # ARREGLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR
    def buscar_ventas(self, cliente=None, productos=None, cantidad=None, pago=None, envio=None):
        ventas_encontradas = []
        for venta in self.ventas:
            if (cliente is None or venta.cliente == cliente) and \
               (productos is None or venta.productos == productos) and \
               (cantidad is None or venta.cantidad == cantidad) and \
               (pago is None or venta.pago == pago) and \
               (envio is None or venta.envio == envio):
                ventas_encontradas.append(venta)
        return ventas_encontradas
    
   
    # FALTA GENERAR FACTURAS