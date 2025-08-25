from datetime import date
from Productos import GestionProductos

class Compras:
    def __init__(self, id_compras, fecha, producto, cantidad):
        self.__id_compras = id_compras
        self.__fecha = fecha
        self.__producto = producto
        self.__cantidad = cantidad


    #Getters
    def get_id_compras(self):
        return self.__id_compras
    def get_fecha(self):
        return self.__fecha

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def __str__(self):
        return (f"Compra ID: {self.__id_compras} | Fecha: {self.__fecha} | "
                f"Producto: {self.__producto.get_nombre_producto()} | "
                f"Cantidad: {self.__cantidad} | Stock después: {self.__producto.get_stock()}")


class DettalesCompras:


    def __init__(self, gestor_productos, gestor_categorias, gestor_proveedores):
        self.listado_compras = {} #este diccionario es para guardar todas las compras relacionadas por ID
        self.gestor_productos = gestor_productos
        self.gestor_categorias = gestor_categorias
        self.gestor_proveedores = gestor_proveedores

    def realizar_compra(self, gestor_productos, gestor_proveedores, gestor_categorias):
        fecha_actual = date.today()
        fin_ingresoC = True
        while fin_ingresoC:
            try:

                gestor_productos.agregar_productos(gestor_categorias, gestor_proveedores)
            except Exception as e:
                print('Error - por favor verifique la entrada')

    def mostrar_historial(self):
        if not self.listado_compras:
            print('Aún no se ha realizado compras')
            return
        else:
            for tmp in self.listado_compras.values():
                print(tmp)