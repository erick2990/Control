class Proveedor:
    def __init__(self, id_prov, nombre_prov, empresa_prov, cel_prov, dir_prov, correo_prov):
        self.__id_prov = id_prov
        self.__nombre_prov = nombre_prov
        self.__empresa_prov = empresa_prov
        self.__cel_prov = cel_prov
        self.__dir_prov = dir_prov
        self.__correo_prov = correo_prov
        self.listado_categorias = {} #Se inicializa un diccioanrio vació por si el proveedor

    def get_id_prov(self):
        return self.__id_prov
    def get_nombre_prov(self):
        return self.__nombre_prov
    def get_empresa_prov(self):
        return self.__empresa_prov
    def get_cel_prov(self):
        return self.__cel_prov
    def get_dir_prov(self):
        return self.__dir_prov
    def get_correo_prov(self):
        return self.__correo_prov


class GestionProveedores:

    def __init__(self):
        self.listado_proveedores = {} #Este es el listado de proveedores


    def agregar_proveedor(self):
        fin_prov = True
        print('\t\t\tBienvenido a agregar Proveedor: ')
        print('Ingrese los datos correspondientes \n')

        while fin_prov:
            try:
                while True:
                    id_proveedor = input('Ingrese el ID')
                    if id_proveedor in self.listado_proveedores:
                        print('Este ID ya fue asignado por favor intente con uno nuevo')
                    elif id_proveedor == "":
                        print('Este campo no puede estar vació')
                    else:
                        break
                while True:
                    nombre_p= input('Ingrese el nombre: ')
                    if nombre_p =="":
                        print('Este campo no puede estar vació')
                    else:
                        break
                while True:
                    empresa_p = input('Ingrese el nombre de la empresa: ')
                    if empresa_p =="":
                        print('Este campo no puede estar vació')
                    else:
                        break
                while True:
                    cel_p = input('Ingrese el numero de celular: ')
                    if cel_p =="":
                        print('Este campo no puede estar vació')
                    else:
                        break
                while True:
                    dir_p = input('Ingrese la dirección: ')
                    if dir_p =="":
                        print('Este campo no puede estar vació')
                    else:
                        break
                while True:
                    correo_p = input('Ingrese el correo electrónico')
                    if correo_p =="":
                        print('Este campo no puede estar vació')
                    else:
                        break
                proveedor_tmp = Proveedor(id_proveedor, nombre_p, empresa_p, cel_p, dir_p, correo_p)
                self.listado_proveedores[id_proveedor] = {
                    "Proveedor" : proveedor_tmp
                }

            except Exception as e:
                print('Error por favor verifique la entrada')

            respuesta = input(
                "¿Desea agregar otro proveedor? (S/N): ").strip().upper()  # Si el usuario desea ingresar otro proveedor
            if respuesta != "S":
                print('\t\t\t¡¡¡Proveedores agregados con exito!!!')
                fin_prov = False
            else:
                pass

    def asociar_categorias(self, id_prov ,cantidad):
        proveedor = self.listado_proveedores[id_prov]["Proveedor"]
        cat_ascociadas = proveedor.listado_categorias

        for i in range(1, cantidad + 1):
            print(f'Ingrese la {i}ª categoría:')
            cat_id = input('Ingresa el ID de la categoría que deseas asociar: ').strip()
            cat_nombre = input('Ingresa el nombre de la categoría: ').strip()

            if cat_id in cat_ascociadas:
                print('Esta categoria ya se asocio con el proveedor ')
            else:
                cat_ascociadas[cat_id] = cat_nombre
                print('¡¡¡Categoría asociada con exito!!!')





