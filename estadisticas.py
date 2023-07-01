from collections import Counter
from datetime import datetime
import json
from collections import defaultdict

class Estadisticas:
    def __init__(self, ventas, pagos, envios):
        self.ventas = ventas
        self.pagos = pagos
        self.envios = envios

    def generar_informe_ventas(self):
        clientes_frecuentes = Counter([venta['cliente'] for venta in self.ventas])

        return clientes_frecuentes

    def generar_informe_pagos(self):
        
   
        ventas_por_cliente = Counter({venta['cliente']: venta['total'] for venta in self.ventas})
        pagos_por_cliente = Counter({pago['cliente']: pago['monto'] for pago in self.pagos})
        clientes_con_pagos_pendientes = {cliente: ventas_por_cliente[cliente] - pagos_por_cliente[cliente] for cliente in ventas_por_cliente if ventas_por_cliente[cliente] > pagos_por_cliente[cliente]}

        return clientes_con_pagos_pendientes

    def producto_mas_enviado(self):
        with open('ventas.json', 'r') as f:
            ventas = json.load(f)

        
        todos_productos = [producto for venta in ventas for producto in venta['productos'].split(',')]

        conteo_productos = Counter(todos_productos)

        max_conteo = max(conteo_productos.values())
        productos_mas_vendidos = [producto for producto, conteo in conteo_productos.items() if conteo == max_conteo]

        return productos_mas_vendidos
        
    

    
    def generar_informe_envios(self):
        envios_por_fecha = Counter([datetime.strptime(envio.fecha, '%d/%m/%Y') for envio in self.envios])
        productos_mas_enviados = Counter()
        for envio in self.envios:
            order_compra = self.gestion_ventas.get_venta_by_id(envio.order_compra)
            if order_compra:
                for producto in order_compra.productos:
                    productos_mas_enviados[producto] += 1
        ventas_por_cliente = Counter([venta.cliente for venta in self.ventas])
        envios_por_cliente = Counter([envio.cliente for envio in self.envios])
        clientes_con_envios_pendientes = {cliente: ventas_por_cliente[cliente] - envios_por_cliente[cliente] for cliente in ventas_por_cliente if ventas_por_cliente[cliente] > envios_por_cliente[cliente]}
        return envios_por_fecha, productos_mas_enviados, clientes_con_envios_pendientes


    def total_ventas_por_ano(json_file):
        with open('ventas.json', 'r') as f:
            ventas = json.load(f)

        ventas_por_ano = defaultdict(float)

        for venta in ventas:
            fecha = datetime.strptime(venta['fecha'], '%d/%m/%Y')
            ventas_por_ano[fecha.year] += venta['total']

        for year, total in ventas_por_ano.items():
            print(f"Total en ventas del {year}: {total}")

    def total_ventas_por_mes(json_file):
        with open('ventas.json', 'r') as f:
            ventas = json.load(f)

        ventas_por_mes = defaultdict(float)

        for venta in ventas:
            fecha = datetime.strptime(venta['fecha'], '%d/%m/%Y')
            ventas_por_mes[(fecha.year, fecha.month)] += venta['total']

        for (year, month), total in ventas_por_mes.items():
            print(f"Total en ventas del mes: {month}/{year}: {total}")

    def total_ventas_por_dia(json_file):
        with open('ventas.json', 'r') as f:
            ventas = json.load(f)

        ventas_por_dia = defaultdict(float)

        for venta in ventas:
            fecha = datetime.strptime(venta['fecha'], '%d/%m/%Y')
            ventas_por_dia[(fecha.year, fecha.month, fecha.day)] += venta['total']

        for (year, month, day), total in ventas_por_dia.items():
            print(f"Total en ventas el: {day}/{month}/{year}: {total}")

    def total_pagos_por_ano(json_file):
        with open('pagos.json', 'r') as f:
            pagos = json.load(f)

        pagos_por_ano = defaultdict(float)

        for pago in pagos:
            fecha = datetime.strptime(pago['fecha'], '%d/%m/%Y')
            pagos_por_ano[fecha.year] += pago['monto']

        for year, total in pagos_por_ano.items():
            print(f"Total en pagos del {year}: {total}")


    def total_pagos_por_mes(json_file):
        with open('pagos.json', 'r') as f:
            pagos = json.load(f)

        pagos_por_mes = defaultdict(float)

        for pago in pagos:
            fecha = datetime.strptime(pago['fecha'], '%d/%m/%Y')
            pagos_por_mes[(fecha.year, fecha.month)] += pago['monto']

        for (year, month), total in pagos_por_mes.items():
            print(f"Total en pagos del mes {month} del año {year}: {total}")

  
    def total_pagos_por_dia(json_file):
        with open('pagos.json', 'r') as f:
            pagos = json.load(f)

        pagos_por_dia = defaultdict(float)

        for pago in pagos:
            fecha = datetime.strptime(pago['fecha'], '%d/%m/%Y')
            pagos_por_dia[(fecha.year, fecha.month, fecha.day)] += pago['monto']

        for (year, month, day), total in pagos_por_dia.items():
            print(f"Total en pagos del día {day} del mes {month} del año {year}: {total}")

    def total_envios_por_ano(json_file):
        with open('envios.json', 'r') as f:
            envios = json.load(f)

        envios_por_ano = defaultdict(int)

        for envio in envios:
            fecha = datetime.strptime(envio['fecha'], '%d/%m/%Y')
            envios_por_ano[fecha.year] += 1

        for year, total in envios_por_ano.items():
            print(f"Total de envíos del año {year}: {total}")


    def total_envios_por_mes(json_file):
        with open('envios.json', 'r') as f:
            envios = json.load(f)

        envios_por_mes = defaultdict(int)

        for envio in envios:
            fecha = datetime.strptime(envio['fecha'], '%d/%m/%Y')
            envios_por_mes[(fecha.year, fecha.month)] += 1

        for (year, month), total in envios_por_mes.items():
            print(f"Total de envíos del mes {month} del año {year}: {total}")

    
    def total_envios_por_dia(json_file):
        with open('envios.json', 'r') as f:
            envios = json.load(f)

        envios_por_dia = defaultdict(int)

        for envio in envios:
            fecha = datetime.strptime(envio['fecha'], '%d/%m/%Y')
            envios_por_dia[(fecha.year, fecha.month, fecha.day)] += 1

        for (year, month, day), total in envios_por_dia.items():
            print(f"Total de envíos del día {day} del mes {month} del año {year}: {total}")

