from suma import *


def test_vacio():
    assert suma("") == 0


def test_un_numero():
    assert suma("7") == 7


def test_dos_numeros():
    assert suma("7,3") == 10


def test_tres_numeros():
    assert suma("2,4,4") == 10


def test_cuatro_numeros():
    assert suma("1,2,3,4") == 10


def test_cinco_numeros():
    assert suma("5,6,7,8,9") == 35


def test_raro():
    assert suma("1,2,4\n5,6") == 18
