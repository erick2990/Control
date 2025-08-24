class Admin:
    def __init__(self, user, password):
        self.__user =  user
        self.__password = password



    def agregar_productos(self):
        fin_agregar = True

        while fin_agregar:
            print('Proceso de añadir productos')