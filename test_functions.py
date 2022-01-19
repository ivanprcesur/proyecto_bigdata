from src.main.utils.functions import sumar
from src.main.utils.functions import restar
from src.main.utils.functions import multiplicacion
from src.main.utils.functions import division
from src.main.utils.functions import potencia
from src.main.utils.functions import longitud
from src.main.utils.functions import sumar_numeros



def test_sumar1():
    assert sumar(1, 2) == 3

def test_sumar2():
    assert sumar(3, 4) == 7

def test_restar():
    assert restar(8, 4) == 4

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12

def test_division1():
    assert division(4, 2) == 2

def test_potencia():
    assert pow(4,2) == 16

def test_longitud():
    assert len('ivan') == 4

def test_sumar_numeros():
    assert sum([5,5]) == 10