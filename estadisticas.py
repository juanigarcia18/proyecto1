class Estadisticas:
    def __init__(self, ventas, pagos, envios):
        self.ventas = ventas
        self.pagos = pagos
        self.envios = envios

    def generar_informe_ventas(self, inicio, fin):
        ventas_periodo = [venta for venta in self.ventas if inicio <= venta.fecha <= fin]
        return len(ventas_periodo)

    def generar_informe_pagos(self, inicio, fin):
        pagos_periodo = [pago for pago in self.pagos if inicio <= pago.fecha <= fin]
        return len(pagos_periodo)

    def generar_informe_envios(self, inicio, fin):
        envios_periodo = [envio for envio in self.envios if inicio <= envio.fecha <= fin]
        return len(envios_periodo)
