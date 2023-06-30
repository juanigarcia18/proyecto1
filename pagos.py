import json

class Pago:
    def __init__(self, cliente, monto, moneda, tipo, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo = tipo
        self.fecha = fecha
    
    def __str__(self):
        return f"Cliente: {self.cliente}\nMonto: {self.monto}\nMoneda: {self.moneda}\nTipo de pago: {self.tipo}\nFecha del pago: {self.fecha}"

class GestionPagos:
    def __init__(self):
        self.pagos = []

    def registrar_pago(self, cliente, monto, moneda, tipo, fecha):
        pago = Pago(cliente, monto, moneda, tipo, fecha)
        self.pagos.append(pago)
        self.guardar_pagos_json()

    def buscar_pago(self, cliente=None, fecha=None, tipo=None, moneda=None):
        resultados = []
        for pago in self.pagos:
            if (cliente is None or pago.cliente == cliente) and \
                (fecha is None or pago.fecha == fecha) and \
                (tipo is None or pago.tipo == tipo) and \
                (moneda is None or pago.moneda == moneda):
                resultados.append(pago)
        return resultados
    def registrar_pago(self, cliente, monto, moneda, tipo, fecha):
        pago = Pago(cliente, monto, moneda, tipo, fecha)
        self.pagos.append(pago)
    
    def guardar_pagos_json(self):
        pagos_dict = [vars(pago) for pago in self.pagos]
        with open("envios.json", 'w') as f:
            json.dump(pagos_dict, f)

