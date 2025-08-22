class Compras:
    def __init__(self, id_compras, fecha, id_proveedor, id_empleado, total):
        self.__id_compras = id_compras
        self.__fecha = fecha
        self.__id_proveedor = id_proveedor
        self.__id_empleado = id_empleado
        self.__total = total

    #Getters
    def get_id_compras(self):
        return self.__id_compras
    def get_fecha(self):
        return self.__fecha
    def get_id_proveedor(self):
        return self.__id_proveedor
    def get_id_empleado(self):
        return self.__id_empleado
    def get_total(self):
        return self.__total

    #Setters

    def set_total(self, nuevo_total):
        if nuevo_total>0:
            print('total actualizado')
            self.__total = nuevo_total
        else:
            print('El total no puede ser menor que 0')