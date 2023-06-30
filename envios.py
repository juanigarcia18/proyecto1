import json
import os

class Envio:
    def __init__(self, cliente, order_compra, servicio, costo, direccion=None, motorizado=None, fecha=None):
        self.order_compra = order_compra
        self.servicio = servicio
        self.costo = costo
        self.direccion = direccion
        self.motorizado = motorizado
        self.fecha = fecha
        self.cliente = cliente

    def __str__(self):
        return f"Orden de compra: {self.order_compra}\nServicio: {self.servicio}\nDirección: {self.direccion}\nMotorizado: {self.motorizado}\nFecha: {self.fecha}\n"


class GestionEnvios:
    def __init__(self):
        self.envios = []
        self.cargar_envios_desde_json()

    def guardar_envios_json(self):
        envios_dict = [vars(envio) for envio in self.envios]
        with open("envios.json", 'w') as f:
            json.dump(envios_dict, f)


    def registrar_envio(self, cliente, order_compra, servicio, costo, direccion=None, motorizado=None, fecha=None):
        envio = Envio(cliente, order_compra, servicio, costo, direccion, motorizado, fecha)
        self.envios.append(envio)
        self.guardar_envios_json()


    def buscar_envios(self, cliente=None, fecha=None):
        resultados = []
        for envio in self.envios:
            if (cliente is None or envio.cliente == cliente) and (fecha is None or envio.fecha == fecha):
                resultados.append(envio)
        return resultados

    def cargar_envios_desde_json(self):
        if os.path.isfile('envios.json'):
            with open('envios.json', 'r') as f:
                envios_dict = json.load(f)
                for envio in envios_dict:
                    self.registrar_envio(envio['cliente'],envio['order_compra'], envio['servicio'], envio['costo'], envio['direccion'], envio['motorizado'], envio['fecha'])

