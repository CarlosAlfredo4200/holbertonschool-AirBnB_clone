import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_name(self):
        # Crear una instancia de State
        state = State()

        # Establecer el nombre del estado
        state.name = ""

        # Verificar si el nombre del estado es correcto
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
