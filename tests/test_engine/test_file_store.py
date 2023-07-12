import datetime
import unittest
import os
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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

    # def test_objects_default_value(self):
    #      self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all_returns_dictionary_of_objects(self):
        self.storage.new(self.base_model)
        objects = self.storage.all()
        self.assertEqual(objects, {f"BaseModel.{self.base_model.id}": self.base_model})

    def test_new_adds_object_to_objects_dictionary(self):
        self.storage.new(self.base_model)
        expected_key = f"BaseModel.{self.base_model.id}"
        self.assertIn(expected_key, self.storage._FileStorage__objects)
        self.assertEqual(
            str(self.storage._FileStorage__objects[expected_key]),
            str(self.base_model)
        )

    # def test_save_creates_file_with_correct_data(self):
    #     self.storage.new(self.base_model)
    #     self.storage.save()
    #     with open(self.file_path, "r") as file:
    #         data = json.load(file)
    #         expected_data = {
    #             f"BaseModel.{self.base_model.id}": self.base_model.to_dict()
    #         }
    #         self.assertEqual(data, expected_data)

    # def test_reload_loads_data_from_file(self):
    #     self.storage.new(self.base_model)
    #     self.storage.save()
    #     self.storage.new(BaseModel())
    #     self.storage.reload()
    #     self.assertEqual(
    #         self.storage._FileStorage__objects,
    #         {f"BaseModel.{self.base_model.id}": self.base_model}
    #     )

class TestBaseModel(unittest.TestCase):
    def test_init_assigns_unique_id_and_datetimes(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime.datetime)
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

    def test_str_returns_correct_string_representation(self):
        base_model = BaseModel()
        expected_output = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_output)

    def test_save_updates_updated_at(self):
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)

    def test_to_dict_returns_correct_dict_representation(self):
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["created_at"], base_model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], base_model.updated_at.isoformat())

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)
            
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        
if __name__ == '__main__':
    unittest.main()