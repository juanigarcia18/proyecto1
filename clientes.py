import json

class Cliente:
    def __init__(self, nombre, tipo_cliente, documento, correo, direccion, telefono):
        
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.documento = documento
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}\nTipo de cliente: {self.tipo_cliente}\nDocumento: {self.documento}\nCorreo: {self.correo}\nDirección: {self.direccion}\nTeléfono: {self.telefono}"


class GestionClientes:
    def __init__(self):
        self.clientes = []
        self.cargar_clientes()

    def guardar_clientes(self):
        clientes_data = []
        for cliente in self.clientes:
            cliente_data = {
                'nombre': cliente.nombre,
                'tipo_cliente': cliente.tipo_cliente,
                'documento': cliente.documento,
                'correo': cliente.correo,
                'direccion': cliente.direccion,
                'telefono': cliente.telefono
            }
            clientes_data.append(cliente_data)

        with open('clientes.json', 'w') as f:
            json.dump(clientes_data, f, indent=4)

    def cargar_clientes(self):
        try:
            with open('clientes.json', 'r') as f:
                clientes_data = json.load(f)
                for cliente_data in clientes_data:
                    cliente = Cliente(
                        nombre=cliente_data['nombre'],
                        tipo_cliente=cliente_data['tipo_cliente'],
                        documento=cliente_data['documento'],
                        correo=cliente_data['correo'],
                        direccion=cliente_data['direccion'],
                        telefono=cliente_data['telefono']
                    )
                    self.clientes.append(cliente)
        except FileNotFoundError:
            self.clientes = []

    def agregar_cliente(self, nombre, tipo_cliente, documento, correo, direccion, telefono):
        cliente = Cliente(nombre, tipo_cliente, documento, correo, direccion, telefono)
        self.clientes.append(cliente)
        self.guardar_clientes()

    def buscar_cliente(self, documento=None, correo=None):
        resultados = []
        for cliente in self.clientes:
            if documento and cliente.documento == documento:
                resultados.append(cliente)
            if correo and cliente.correo == correo:
                resultados.append(cliente)
        return resultados

    def buscar_nombre_cliente_por_documento(self, documento):
        for cliente in self.clientes:
            if cliente.documento == documento:
                return cliente.nombre
        return None
    
    def buscar_direccion_por_documento(self, documento):
        for cliente in self.clientes:
            if cliente.documento == documento:
                return cliente.direccion
        return None
