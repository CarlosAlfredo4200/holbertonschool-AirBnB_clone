import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModal(unittest.TestCase):

    def test_type_classBaseModal(self):
        self.assertEqual(BaseModel, type(BaseModel()))


if __name__ == '__main__':
    unittest.main()
