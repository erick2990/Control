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


    def __init__(self, gestor_productos):
        self.listado_compras = {} #este diccionario es para guardar todas las compras relacionadas por ID
        self.gestor_productos = gestor_productos

    def realizar_compra(self):
        fecha_actual = date.today()

        fin_ingresoC = True
        while fin_ingresoC:
            try:

                while True:
                    id_compra = input('Ingrese el numero de compra')
                    if id_compra in self.listado_compras:
                        print('Este ID ya existe en el historial de compras')
                    elif id_compra =="":
                        print('Este campo no puede quedar vacio')
                    else:
                        break

                id_producto = input("Ingrese el ID del producto: ").strip()
                producto_total = self.gestor_productos.lista_generalP.get(id_producto)

                if not producto_total:
                    print("Producto no encontrado.")
                    return

                producto = producto_total["Articulo"] #Si el arcitulo si existe entonces pasa

                try:
                    cantidad = int(input("Ingrese la cantidad comprada: "))
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a cero.")
                        return
                except ValueError:
                    print(" Error entrada inválida. Debe ingresar un número entero.")
                    return

                # Actualizar stock y compras
                nuevo_stock = producto.get_stock() + cantidad #al crearse el producto o si ya existe se actualiza el stock
                producto.set_stock(nuevo_stock) #se setea el stock
                producto._Productos__t_compras += cantidad  # acceso directo si no hay setter

                # Crear y guardar la compra
                compra_tmp = Compras(id_compra, fecha_actual, producto, cantidad)
                self.listado_compras[id_compra] = compra_tmp

                print(f"✅ Compra registrada exitosamente. Nuevo stock: {nuevo_stock}")


            except Exception as e:
                print('Error - por favor verifique la entrada')

    def mostrar_historial(self):
        if not self.listado_compras:
            print('Aún no se ha realizado compras')
            return
        else:
            for tmp in self.listado_compras.values():
                print(tmp)