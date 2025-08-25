from datetime import date

class DetallesCompras:


    def __init__(self, gestor_productos, gestor_categorias, gestor_proveedores):
        self.historial  = [] #aqui se guarda el historial de compras
        self.listado_compras = {} #este diccionario es para guardar todas las compras relacionadas por ID
        self.gestor_productos = gestor_productos
        self.gestor_categorias = gestor_categorias
        self.gestor_proveedores = gestor_proveedores

    def realizar_compra(self):
        fecha_actual = date.today()
        fin_ingresoC = True
        while fin_ingresoC:
            try:
                while True:
                    id_compra = input('Ingrese el id de compra: ')
                    if id_compra in self.listado_compras:
                        print('Este registro ya existe por favor verifique')
                    else:
                        print('¡¡¡Registro guardado!!!')
                        break
                gestor_productos.agregar_productos(gestor_categorias, gestor_proveedores)
                fin_ingresoC = False


            except Exception as e:
                print('Error - por favor verifique la entrada')

    def mostrar_historial(self):
        if not self.listado_compras:
            print('Aún no se ha realizado compras')
            return
        else:
            for tmp in self.listado_compras.values():
                print(tmp)