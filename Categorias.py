
class Categorias:
    def __init__(self, id_cat, nombre_cat):
        self.__id_categoria = id_cat
        self.__nombre_cat = nombre_cat

    def get_nombre_cat(self):
        return self.__nombre_cat

    def get_id_categoria(self):
        return self.__id_categoria


class GestionCategorias:

    def __init__(self):
        self.categorias = {}  # Diccionario para productos que coinciden con dicha categoria


    def agregar_categoria(self):
        fin_cat = True
        print('\t\t\tBienvenido a agregar categorías: ')
        while fin_cat:
            try:
                while True:
                    id_cat = input('Ingrese el ID de la categoria: ')
                    if id_cat =="":
                        print('Debe ingresar un dato valido')
                    elif id_cat in self.categorias:
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
                self.categorias[id_cat] = categoria_tmp
                print('¡¡Categoria guardada!!')
            except Exception as e:
                print('Error por favor ingrese un dato valido')
            respuesta = input("¿Desea agregar otra categoria? (S/N): ").strip().upper()  # Si el usuario desea ingresar otra categoria
            if respuesta != "S":
                print('\t\t\t¡¡¡Categorias agregados con exito!!!')
                fin_cat= False
            else:
               pass

    def get_categorias(self):
        return self.categorias

    def ver_categorias(self):
        print('\t\t\tCategorias disponibles: ')
        for x in self.categorias.values():
            print(f'ID: {x.get_id_categoria()} Nombre: {x.get_nombre_cat} ')
