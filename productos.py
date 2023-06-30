import requests
import json
import os

class Producto:
    def __init__(self, name, description, price, category, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.quantity = quantity
    
    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nCategory: {self.category}\nQuantity: {self.quantity}"

class GestionProductos:
    def __init__(self):
        self.productos = []
        self.cargar_productos_desde_json()

    def agregar_producto(self, name, description, price, category, quantity):
        producto = Producto(name, description, price, category, quantity)
        self.productos.append(producto)
        self.guardar_productos_json()

    def obtener_productos_api(self):
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json')
        data = response.json()
        for item in data:
            self.agregar_producto(item['name'], item['description'], item['price'], item['category'], item['quantity'])

    # El método guardar_productos_json convierte cada producto en un diccionario usando la función vars() y luego guarda la lista de diccionarios en el archivo productos.json usando
    # json.dump().
    # El método cargar_productos_desde_json abre el archivo productos.json, carga la lista de diccionarios usando json.load(), y luego agrega cada producto a la lista de productos.
    
    def guardar_productos_json(self):
        productos_dict = [vars(producto) for producto in self.productos]
        with open("productos.json", 'w') as f:
            json.dump(productos_dict, f)

    def buscar_producto(self, name=None, category=None):
        resultados = []
        for producto in self.productos:
            if (name is None or producto.name == name) and (category is None or producto.category == category):
                resultados.append(producto)
        return resultados

    def modificar_producto(self, name, new_name=None, new_description=None, new_price=None, new_category=None, new_quantity=None):
        for i, producto in enumerate(self.productos):
            if producto.name == name:
                if new_name is not None:
                    producto.name = new_name
                if new_description is not None:
                    producto.description = new_description
                if new_price is not None:
                    producto.price = new_price
                if new_category is not None:
                    producto.category = new_category
                if new_quantity is not None:
                    producto.quantity = new_quantity
                self.productos.pop(i)  # Eliminar el producto de la posicion original
                self.productos.insert(i, producto)  # Insertar el producto modificado en la misma posición
                self.guardar_productos_json()
                return True
        return False

    def eliminar_producto(self, name):
        for producto in self.productos:
            if producto.name == name:
                self.productos.remove(producto)
                self.guardar_productos_json()
                return True
        return False
    
    def cargar_productos_desde_json(self):
        if os.path.isfile('productos.json'):
            with open('productos.json', 'r') as f:
                productos_dict = json.load(f)
                for producto in productos_dict:
                    self.agregar_producto(producto['name'], producto['description'], producto['price'], producto['category'], producto['quantity'])


    def obtener_precio_producto(self, nombre_productos):
        with open('productos.json', 'r') as f:
            productos = json.load(f)

        for producto in productos:
            if producto['name'] == nombre_productos:
                return int(producto['price'])  # Asegúrate de que el precio es un número entero

        return None
    
