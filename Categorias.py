from csv import excel_tab
from logging import exception


class Categorias:
    def __init__(self, id_cat, nombre_cat):
        self.__id_categoria = id_cat
        self.__nombre_cat = nombre_cat
        self.__articulos= {} #Diccionario que se vinculara a los productos que pertenecer a esta categoria

    def get_nombre_cat(self):
        return self.__nombre_cat

    def get_id_categoria(self):
        return self.__id_categoria

    def get_articulos(self):
        return self.__articulos

    def __str__(self):
        return f"Categoría: {self.__nombre_cat} | Código: {self.__id_categoria} | Productos: {len(self.__articulos)}"


class GestionCategorias:

    def __init__(self):
        self.__categorias = {}  # Diccionario para productos que coinciden con dicha categoria

    def agregar_categoria(self):
        fin_cat = True
        print('\t\t\tBienvenido a agregar categorías: ')
        while fin_cat:
            try:
                while True:
                    id_cat = input('Ingrese el ID de la categoria: ')
                    if id_cat =="":
                        print('Debe ingresar un dato valido')
                    elif id_cat in self.__categorias:
                        print('Este ID de categoria ya existe, intente con otro')
                    else:
                        break
                while True:
                    nombre_cat = input('Ingrese el nombre de la categoria: ')
                    if nombre_cat == "":
                        print('Debe ingresar un dato valido')
                    else:
                        break
                categoria_tmp  = Categorias(id_cat, nombre_cat) #Objeto tipo categoria
                self.__categorias[id_cat] = {
                    "Categoria":categoria_tmp
                }
            except Exception as e:
                print('Error por favor ingrese un dato valido')

            respuesta = input("¿Desea agregar otra categoria? (S/N): ").strip().upper()  # Si el usuario desea ingresar otra categoria
            if respuesta != "S":
                print('\t\t\t¡¡¡Productos agregados con exito!!!')
                fin_cat= False
            else:
               pass

    def agregar_producto_a_categoria(self, id_cat, id_producto, nombre_producto):
        if id_cat in self.__categorias:
            categoria = self.__categorias[id_cat]["Categoria"] #Aqui se invoca el diccionario de productos de dicho id
            articulos = categoria.get_articulos() #Esto lo devuelve del diccionario de articulos que tiene contenido
            if id_producto in articulos:
                print("Este producto ya existe en la categoría.")
            else:
                articulos[id_producto] = nombre_producto
                print(f'Producto "{nombre_producto}" agregado a la categoría "{categoria.get_nombre_cat()}".')
        else:
            print("La categoría no existe.")