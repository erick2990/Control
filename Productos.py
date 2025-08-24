class Productos:
    def __init__(self,id_p, nombre_p, id_cat, precio_compra, precio_venta, t_compras, t_ventas, stock):
        self.__id_producto = id_p
        self.__nombre_producto = nombre_p
        self.__id_categoria = id_cat
        self.__precio_compra = precio_compra
        self.__precio_venta = precio_venta
        self.__t_compras = t_compras
        self.__t_ventas = t_ventas
        self.__stock = stock

    # Getters
    def get_id_producto(self):
        return self.__id_producto #este id sera escencial para regresar el id

    def get_nombre_producto(self):
        return self.__nombre_producto

    def get_id_categoria(self):
        return self.__id_categoria #este id nos servira para vincular con la categoria correspondiente

    def get_precio_compra(self):
        return self.__precio_compra
    def get_precio_venta(self):
        return self.__precio_venta

    def get_t_compras(self):
        return self.__t_compras

    def get_t_ventas(self):
        return self.__t_ventas

    def get_stock(self):
        return self.__stock

    # Setters
    def set_precio_compra(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio_compra = nuevo_precio
    def set_precio_venta(self, nuevo_precio):
        if nuevo_precio>=0:
            self.__precio_venta = nuevo_precio

    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock

    def __str__(self):
        return (
            f"Producto: {self.__nombre_producto} | Código: {self.__id_producto} | "
            f"Categoría: {self.__id_categoria} | Precio: Q{self.__precio} | "
            f"Compras: {self.__t_compras} | Ventas: {self.__t_ventas} | Stock: {self.__stock}"
        )


class GestionProductos:

    def __init__(self):
        lista_generalP = {} #Se guardaran todos los prodcutos en general

    def agregar_productos(self):
        fin_agregaar =  True
        cantidad = 1
        print('Bienvenido a agregar productos: ')
        while fin_agregaar:
            print(f'\t\t\tAgregue el {cantidad} producto: ')
            while True:
                id_producto = input('Ingrese el ID: ')
                if id_producto == "":
                    print('Por favor ingrese un dato valido')
                else:
                    break
            while True:
                nombre_producto = input('Ingrese le nombre: ')
                if nombre_producto =="":
                    print('Por favor ingrese un dato valido')
                else:
                    break
            while True:
                id_categoria = input('Ingrese la categoria ')
                if id_categoria == "":
                    print('Por favor ingrese un dato valido')
                else:
                    break
            while True:
                try:
                    precio_producto_compra = float(input('Ingrese el precio de compra en Q.'))
                    if precio_producto_compra<=0:
                        print('El precio de compra debe ser mayor a 0')
                    else:
                        break
                except Exception as e:
                    print('Ocurrio un error por favor vuelva a intentarlo')
            while True:
                try:
                    precio_producto_venta = float(input('Ingrese el precio de venta en Q.'))
                    if precio_producto_venta>0 and precio_producto_venta>precio_producto_compra:
                        #Aqui debe cumplirse que el precio debe ser mayor a 0 y tambien debe sacarle una ganancia
                        break
                    else:
                        print('El precio de venta debe ser mayor que el de venta y  debe ser mayor a 0')

                except Exception as e:
                    print('Ocurrio un error por favor vuelva a intentarlo')
            while True:
                try:










