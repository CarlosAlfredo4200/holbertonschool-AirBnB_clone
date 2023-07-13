import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
import os
import json
import models

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

    def test_type_classBaseModal(self):
        self.assertEqual(BaseModel, type(BaseModel()))

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.join(os.getcwd(), "test_file.json")
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_path_default_value(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_file_path(self):
        """
        Test that __file_path attribute is set correctly.
        """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_all_returns_dictionary_of_objects(self):
        self.storage.new(self.base_model)
        objects = self.storage.all()
        self.assertEqual(
            objects, {f"BaseModel.{self.base_model.id}": self.base_model})

    def test_new_adds_object_to_objects_dictionary(self):
        self.storage.new(self.base_model)
        expected_key = f"BaseModel.{self.base_model.id}"
        self.assertIn(expected_key, self.storage._FileStorage__objects)
        self.assertEqual(
            str(self.storage._FileStorage__objects[expected_key]),
            str(self.base_model)
        )

    def test_all(self):
        all_objs = self.storage.all()
        self.assertEqual(all_objs, self.storage._FileStorage__objects)

    def test_new(self):
        bm = BaseModel()
        us = User()
         
        models.storage.new(bm)
        models.storage.new(us)
         
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
    
    def test_file_path_none_returns_ok(self):
        storage = FileStorage()
        storage._FileStorage__file_path = None
        result = storage.save()
        self.assertEqual(result, "OK")
        
if __name__ == '__main__':
    unittest.main()
