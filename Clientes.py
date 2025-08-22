from enum import nonmember


class Clientes:

    def __init__(self, nit , nombre_cliente, cel, direccion, correo ):
        self.__nit = nit
        self.__nombre_cliente = nombre_cliente
        self.__cel= cel
        self.__direccion = direccion
        self.__correo = correo
        self.__clientes = {}

    # Getters
    def get_nit(self):
        return self.__nit
    def get_nombre_cliente(self):
        return self.__nombre_cliente
    def get_cel(self):
        return self.__cel
    def get_direccion(self):
        return self.__direccion
    def get_correo(self):
        return self.__correo

    # Setter
    def set_cel(self, nuevo_cel):
        if nuevo_cel != self.__cel:
            print('Actualizacion de datos')
            self.__cel = nuevo_cel
        else:
            print('Numero repetido por favor intente de nuevo')
    def set_direccion(self, nueva_direccion):
        if nueva_direccion.lower() != self.__direccion:
            print('Direccion actualizada con exito')
        else:
            print('La direccion coincide con la anterior por favor intente de nuevo')

