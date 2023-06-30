class Envio:
    def __init__(self, order_compra, servicio, costo):
        self.order_compra = order_compra
        self.servicio = servicio
        self.costo = costo


    def __str__(self):
        return f"Orden de compra: {self.order_compra}\nServicio: {self.servicio}\nDireccion: {self.direccion}\nestado: {self.estado}\n"


class GestionEnvios:
    def __init__(self):
        self.envios = []

    def registrar_envio(self, order_compra, servicio, costo):
        envio = Envio(order_compra, servicio, costo)
        self.envios.append(envio)

    
    # REVISAR
    def buscar_envio(self, order_compra=None, servicio=None, estado=None):
        resultados = []
        for envio in self.envios:
            if (order_compra is None or envio.order_compra == order_compra) and \
                (servicio is None or envio.servicio == servicio) and \
                (estado is None or envio.estado == estado):
                resultados.append(envio)
        return resultados
    def registrar_envio(self, order_compra, servicio, direccion, estado, motorizado=None):
        envio = Envio(order_compra, servicio, direccion, estado, motorizado)
        self.envios.append(envio)
