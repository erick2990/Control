from Usuarios import Admin, LoginAdmin
from Productos import GestionProductos
from Proveedores import GestionProveedores
from Categorias import GestionCategorias

from Compras import DettalesCompras

class Datos:
    def __init__(self, nombre_em, direccion):
        self.__empresa = nombre_em
        self.__direccion = direccion

    def get_empresa(self):
        return self.__empresa

    def get_direccion(self):
        return self.__direccion

#Esta funcion se encarga de registrar datos basicos de la empresa como el nombre y la direccion
def registrar_empresa():
    while True:
        print('\t\t\tBienvenido al sistema de inventarios')
        nombre_empresa = input('Ingrese el nombre de la empresa: ')
        if nombre_empresa == "":
            print(' Por favor ingrese un nombre válido.')
            continue

        direccion = input('Ingrese la dirección de la empresa: ')
        if direccion == "":
            print('Por favor ingrese una dirección válida.')
            continue

        empresa = Datos(nombre_empresa, direccion)
        print('Datos guardados correctamente.')
        return empresa


#Esta funcion se encarga de realizar el menu principal para iniciar con todo el programa
def menu_principal(empresa):
    fin_principal = True
    #objetos instanciados de las clases de los distintos archivos
    administrador = LoginAdmin()
    gestor_productos = GestionProductos()
    gestor_proveedores = GestionProveedores()
    gestor_categorias = GestionCategorias()

    while fin_principal:
       try:
           print(
               f"\n\tSistema de control para la empresa: {empresa.get_empresa()} ubicada en {empresa.get_direccion()}")
           print("Seleccione un rol para continuar:")
           print("1. Ingresar como Administrador")
           print("2. Ingresar como Cajero")
           print("3. Ingresar como Visitante")
           print("4. Salir del sistema")
           opcion = int(input("Ingrese una opcion: "))

           match opcion:

              case 1:
                   print("Accediendo como Administrador...")
                   if administrador.inicio_sesion():
                       print('Ingreso de forma correcta')
                       administrador.menu(gestor_productos, gestor_proveedores, gestor_categorias)
                       #Estos datos son sobre los que se trabajara, la manipulacion s eejecutara en otros archivos

                   else:
                       print('Intente más tarde')

              case 2:
                   print("Accediendo como Cajero...")

              case 3:
                   print("Accediendo como Visitante...")

              case 4:
                   print('Gracias por usar el sistema')
                   fin_principal = False
              case _:
                   print("Opción inválida. Intente nuevamente.")

       except Exception as e:
           print(f'Error por favor vuelva a intentarlo {e}')

empresa_registrada = registrar_empresa()
menu_principal(empresa_registrada)
