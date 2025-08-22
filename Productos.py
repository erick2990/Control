class Productos:
    def __init__(self,id_p, nombre_p, id_cat, precio, t_compras, t_ventas, stock):
        self.__id_producto = id_p
        self.__nombre_producto = nombre_p
        self.__id_categoria = id_cat
        self.__precio = precio
        self.__t_compras = t_compras
        self.__t_ventas = t_ventas
        self.__stock = stock
        self.__productos = {}

    # Getters
    def get_id_producto(self):
        return self.__id_producto #este id sera escencial para regresar el id

    def get_nombre_producto(self):
        return self.__nombre_producto

    def get_id_categoria(self):
        return self.__id_categoria #este id nos servira para vincular con la categoria correspondiente

    def get_precio(self):
        return self.__precio

    def get_t_compras(self):
        return self.__t_compras

    def get_t_ventas(self):
        return self.__t_ventas

    def get_stock(self):
        return self.__stock

    # Setters
    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio

    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock


    def agregar_producto(self, producto):
        self.__productos[producto.get_id_producto()] = producto #se añade el producto al invenentario general

    def __str__(self):
        return (
            f"Producto: {self.__nombre_producto} | Código: {self.__id_producto} | "
            f"Categoría: {self.__id_categoria} | Precio: Q{self.__precio} | "
            f"Compras: {self.__t_compras} | Ventas: {self.__t_ventas} | Stock: {self.__stock}"
        )

