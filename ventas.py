class Venta:
    iva = 0.16
    igtf = 0.03
    def __init__(self, cliente, productos, cantidad, pago, envio):
        self.cliente = cliente
        self.productos = productos
        self.cantidad = cantidad
        self.pago = pago
        self.envio = envio

class GestionVentas:
    def __init__(self):
        self.ventas = []

    # REVISAR ESTOOOOOO NO PONER ID y no se si esto hace falta
    def guardar_ventas_txt(self):
        with open('ventas.txt', 'w') as f:
            for venta in self.ventas:
                f.write(f'{venta.id},{venta.cliente.id},{[producto.id for producto in venta.productos]}\n')
                
    def registrar_venta(self, cliente, productos, cantidad, pago, envio):
        venta = Venta(cliente, productos, cantidad, pago, envio)
        subtotal = sum(producto.price * cantidad for producto, cantidad in zip(self.productos, self.cantidad))
        descuento = subtotal * 0.05 if self.cliente.tipo == 'juridico' and self.pago == 'contado' else 0
        iva = subtotal * self.IVA
        igtf = subtotal * self.IGTF if self.pago == 'Zelle' or 'Cash' else 0
        total = subtotal - descuento + iva + igtf        
        self.ventas.append(venta, subtotal, descuento, iva, igtf, total)
        return {
            'cliente' : cliente,
            'productos' : productos,
            'cantidad' : cantidad,
            'pago' : pago,
            'envio' : envio,
            'subtotal': subtotal,
            'descuento': descuento,
            'iva': iva,
            'igtf': igtf,
            'total': total
        }
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