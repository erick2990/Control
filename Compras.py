from datetime import date

class Compras:
    def __init__(self, id_compras, fecha):
        self.__id_compras = id_compras
        self.__fecha = fecha


    #Getters
    def get_id_compras(self):
        return self.__id_compras
    def get_fecha(self):
        return self.__fecha


class DettalesCompras:


    def __init__(self):
        self.listado_compras = {} #este diccionario es para guardar todas las compras relacionadas por ID

    def realizar_compra(self):
        fin_ingresoC = True
        while fin_ingresoC:
            try:
                fecha_actual = date.today()
                while True:
                    id_compra = input('Ingrese el numero de compra')
                    if id_compra in self.listado_compras:
                        print('Este ID ya existe en el historial de compras')
                    elif id_compra =="":
                        print('Este campo no puede quedar vacio')
                    else:
                        break
                compra_tmp = Compras(id_compra, fecha_actual,)
                self.listado_compras[id_compra] = {
                    "Compra" : compra_tmp
                }
                fin_ingresoC=False


            except Exception as e:
                print('Error - por favor verifique la entrada')