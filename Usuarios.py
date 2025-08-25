import getpass
from Compras import DetallesCompras


class Admin:
    def __init__(self, usuario, password):
        self.__usuario = usuario
        self.__password = password

    def get_usuario(self):
        return self.__usuario
    def get_password(self):
        return self.__password


class LoginAdmin:
    admin = Admin('Erick', 'Erick2000')

    def inicio_sesion(self):

        intentos = 3
        while intentos>0:
            try:
                user = input('Ingrese su usuario: ')
                password =  getpass.getpass('Ingrese su contraseña')
                if user == self.admin.get_usuario() and password == self.admin.get_password():
                    print('¡¡Inicio de sesión Exitoso!!')
                    return True

                else:
                    intentos -=1
                    print(f'Le quedan {intentos}')
            except Exception as e:
                print('Error por favor verifique la entrada')
        print('Se terminaron los intentos validos')

    #Este menu sirve solo para el admin donde requiere el metodo de gestionar productos y proveedores en este ambito
    # compras se vuelve en la accion de interaccion entre detalles compras por medio de la gestion de producos
    def menu(self, gestor_productos, gestor_proveedores, gestor_categorias):
        compras = DetallesCompras(gestor_productos, gestor_categorias, gestor_proveedores)
        #Es necesario enviar estos dos argumentos para que pueda manipularse tanto el gestor de productos
        #como el gestor de proveedores

        while True:
            print('\n--- Menú Administrador ---')
            print('1. Agregar categorias\n2. Registrar compra\n3. Ver historial de compras')
            print('4. Agregar proveedor\n5. Ver historial de compras\n6. Salir')
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1: #Agregar categorias
                    gestor_categorias.agregar_categoria()
                case 2: #Registrar compras
                    if not gestor_categorias.get_categorias(): #Si categorias o proveedores esta vacio no se puede hacer una compra
                        print('No se pueden realizar compras aún, se necesitan registros de categorias')

                    elif not gestor_proveedores.get_proveedores():
                        print('No se pueden realizar compras aún, se necesitan registros de proveedores')
                    else:
                        compras.realizar_compra()

                case 3: #Historial de compras
                    compras.mostrar_historial()
                case 4: #Agregar proveedores
                    gestor_proveedores.agregar_proveedor()
                case 5:
                    id_prov = input("Ingrese el ID del proveedor: ")
                    if id_prov in gestor_proveedores.listado_proveedores:
                        try:
                            cantidad = int(input("¿Cuántas categorías desea asociar? "))
                            gestor_proveedores.asociar_categorias(id_prov, cantidad)
                        except:
                            print("Cantidad inválida.")
                    else:
                        print("Proveedor no encontrado.")
                case 6:
                    print("Sesión finalizada.")
                    break
                case _:
                    print("Opción inválida.")


