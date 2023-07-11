import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_save_updates_updated_at(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict_with_correct_values(self):
        expected_dict = {
            '__class__': 'BaseModel',
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        }
        obj_dict = self.base_model.to_dict()
        self.assertDictEqual(expected_dict, obj_dict)

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_str(self):
        class_name = self.base_model.__class__.__name__
        expected_output = "[{}] ({}) {}".format(
            class_name, self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_output)



if __name__ == '__main__':
    unittest.main()




