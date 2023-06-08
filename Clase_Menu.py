class Menu:
    __switcher = None

    def __init__(self)->None:
        self.__switcher = {1:self.op1,
                           2:self.op2,
                           3:self.op3,
                        }

    def run(self,Lista):
        band = True
        while band:
            b = int(input("""
Menu Principal:
1-insertar elemento en la lista
2-insertar elemento al final de la lista
3-mostrar elemento segun indice 
0-salir
\n"""))
            func = self.__switcher.get(b)
            if func:
                 func(Lista)
            else:
                print("Saliendo...")
                band = False
    def op1(self,lista):
        lista.insertarElemento()


    def op2(self,lista):
        lista.agregarElemento()

    def op3(self,lista):
        lista.mostrarElemento()