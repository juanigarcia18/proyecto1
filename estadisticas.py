from collections import Counter
from datetime import datetime

class Estadisticas:
    def _init_(self, ventas, pagos, envios):
        self.ventas = ventas
        self.pagos = pagos
        self.envios = envios

    def generar_informe_ventas(self):
         
        ventas_por_fecha = Counter([datetime.strptime(venta['fecha'], '%d/%m/%Y') for venta in self.ventas])

        
        productos_mas_vendidos = Counter([producto for venta in self.ventas for producto in venta['productos']])

        
        clientes_frecuentes = Counter([venta['cliente'] for venta in self.ventas])

        return ventas_por_fecha, productos_mas_vendidos, clientes_frecuentes

    def generar_informe_pagos(self):
        
        pagos_por_fecha = Counter([datetime.strptime(pago['fecha'], '%d/%m/%Y') for pago in self.pagos])

        
        ventas_por_cliente = Counter({venta['cliente']: venta['total'] for venta in self.ventas})
        pagos_por_cliente = Counter({pago['cliente']: pago['monto'] for pago in self.pagos})
        clientes_con_pagos_pendientes = {cliente: ventas_por_cliente[cliente] - pagos_por_cliente[cliente] for cliente in ventas_por_cliente if ventas_por_cliente[cliente] > pagos_por_cliente[cliente]}

        return pagos_por_fecha, clientes_con_pagos_pendientes

    def generar_informe_envios(self):
        
        envios_por_fecha = Counter([datetime.strptime(envio['fecha'], '%d/%m/%Y') for envio in self.envios])

        
        productos_mas_enviados = Counter([producto for envio in self.envios for producto in envio['order_compra']['productos']])

      
        ventas_por_cliente = Counter([venta['cliente'] for venta in self.ventas])
        envios_por_cliente = Counter([envio['cliente'] for envio in self.envios])
        clientes_con_envios_pendientes = {cliente: ventas_por_cliente[cliente] - envios_por_cliente[cliente] for cliente in ventas_por_cliente if ventas_por_cliente[cliente] > envios_por_cliente[cliente]}

        return envios_por_fecha, productos_mas_enviados, clientes_con_envios_pendientes