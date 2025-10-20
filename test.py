import pytest
from calc import suma

def test_suma_numeros():
    assert suma(2, 3) == 5
    assert suma(2.5, 3.5) == 6.0
    assert suma(2, 3.5) == 5.5
    assert suma(2, "texto") == "error"
