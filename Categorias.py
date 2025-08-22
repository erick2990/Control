class Categorias:
    def __init__(self, id_cat, nombre_cat):
        self.__id_categoria = id_cat
        self.__nombre_cat = nombre_cat
        self.__articulos = {}  # Diccionario para productos que coinciden con dicha categoria

    # Getter para nombre
    def get_nombre_cat(self):
        return self.__nombre_cat

    # Getter para ID
    def get_id_categoria(self):
        return self.__id_categoria

    # Getter para artículos
    def get_articulos(self):
        return self.__articulos

    def agregar_producto(self, producto):
        self.__articulos[producto.get_id_producto()] = producto

    def __str__(self):
        return f"Categoría: {self.__nombre_cat} | Código: {self.__id_categoria} | Productos: {len(self.__articulos)}"