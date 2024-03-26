from calculadora import *


def prueba_suma():
    assert suma(5, 8) == 13
    assert suma(-2, -7) == -9
    assert suma(0, 0) == 0
    print("Funcionamiento exitoso")


# _____Llamado a la funcion______#
prueba_suma()
