from zope.interface import Interface
from zope.interface import implementer
from  abc import ABC, abstractmethod
"""la interfaz Icoleccion puede insertar un elemento
el la lista en una poscicion indicada siempre y cuando
este dentro de los limites de ella ta,puede agregar un
elemento al finala de la lista y mostrar un elemento 
segun una posicion especifica los metodos a utilizar son
insertarElemento ()
agregarElemento ()
mostrarElemento ()
"""
class IColeccion (Interface):
    @abstractmethod
    def insertarElemento (self):
        pass

    @abstractmethod
    def agregarElemento (self):
        pass

    @abstractmethod
    def mostrarElemento (self):
        pass
@implementer(IColeccion)
class Lista:
    __lista : list

    def __init__(self)-> None:
        self.__lista = []
#Metodo de la interface IColeccion
    def insertarElemento(self):

        band = True
        while band:
            opc = int(input("desea insertar un elemento 1 = si ; 2 = no\n"))
            if opc == 1:
                try:
                    elemento = int(input("ingrese el valor a ingresar en la lista\n"))
                    indice = int(input("ingrese el lugar donde desa agregar el elemento\n")) - 1
                    self.__lista.insert(indice,elemento)
                except:
                    if indice < 0:
                        print("Error el indice agregado es menor a 0 imposible asignar")
                    elif indice > len(self.__lista):
                        print("Error la posicion agregada exede la cantidad de elementos a almacenar en la lista")
            if opc == 2:
                band = False

    # Metodo de la interface IColeccion
    def agregarElemento(self):
        elemento = int(input("ingrese el elemento a almacenar\n"))
        self.__lista.append(elemento)

    # Metodo de la interface IColeccion
    def mostrarElemento(self):
        indice = int(input(f"ingrese el la posicion del elemento a ver en la lista cantidad de elemntos: {len(self.__lista)}\n "))
        band = True
        while band:
            try:
                print(f"elemento: {self.__lista[indice - 1]} indice:{indice}")
            except:
                print("Error la poscicion acceder para mostrar el elemento exede los limites de la lista")
                indice = int(input(f"ingrese el la posicion del elemento a ver en la lista cantidad de elemntos: {len(self.__lista)}\n "))
            else:
                band = False

