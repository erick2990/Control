class Datos:
    def __init__(self, nombre_em, direccion ):
        self.__empresa = nombre_em
        self.__direccion = direccion

    def get_empresa(self):
        return self.__empresa
    def get_direccion(self):
        return self.__direccion

fin_menu = True


while fin_menu:
    inicio = True

    while inicio:
        try:
            print('Bienvenido a sistema de inventarios:')
            nombre_empresa = input('Ingrese el nombre de la empresa')
            if nombre_empresa == "":
                print('Por favor ingrese un nombre valido')
            else:
                print('Nombre guardado correctamente!!')
                direccion = input('Ingrese la direccion de la empresa: ')
                empresa = Datos(nombre_empresa, direccion)
                inicio = False
        except Exception as e:
            print('error por favor verifique la entrada de datos')

    print(f'sistema de control para la empresa {empresa.get_empresa()}')
    print('Inicialmente se cuenta sin nigun producto por lo que por ahora solo se mostrara la opcion para administrador')

