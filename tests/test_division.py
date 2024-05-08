# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import division

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación division
    def test_division(self):
        assert division(6,2) == 3.0
        assert division(-2,-1) == 2.0
        assert division(-7,2) == -3.5
        assert division(-16,8) == -2
