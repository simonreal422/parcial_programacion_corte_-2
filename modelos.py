class Producto:
    def __init__(self, id_producto, nombre, categoria, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio


class Cliente:
    def __init__(self, id_cliente, nombre, tipo, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.tipo = tipo
        self.telefono = telefono


class Proveedor:
    def __init__(self, id_proveedor, nombre, ciudad):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.ciudad = ciudad