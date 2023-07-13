import datetime
import unittest
import os
import json
<<<<<<< HEAD
=======
import models
>>>>>>> 80145c61fb0c9f412ac438c4bbbc6a8dbd5501d1
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
 

<<<<<<< HEAD
=======

>>>>>>> 80145c61fb0c9f412ac438c4bbbc6a8dbd5501d1
class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = os.path.join(os.getcwd(), "test_file.json")
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

<<<<<<< HEAD
    
    def test_file_path_default_value(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_default_value(self):
         self.assertEqual(self.storage._FileStorage__objects, {})
=======
    def test_file_path_default_value(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_file_path(self):
        """
        Test that __file_path attribute is set correctly.
        """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
>>>>>>> 80145c61fb0c9f412ac438c4bbbc6a8dbd5501d1

    def test_all_returns_dictionary_of_objects(self):
        self.storage.new(self.base_model)
        objects = self.storage.all()
<<<<<<< HEAD
        self.assertEqual(objects, {f"BaseModel.{self.base_model.id}": self.base_model})
=======
        self.assertEqual(
            objects, {f"BaseModel.{self.base_model.id}": self.base_model})
>>>>>>> 80145c61fb0c9f412ac438c4bbbc6a8dbd5501d1

    def test_new_adds_object_to_objects_dictionary(self):
        self.storage.new(self.base_model)
        expected_key = f"BaseModel.{self.base_model.id}"
        self.assertIn(expected_key, self.storage._FileStorage__objects)
        self.assertEqual(
            str(self.storage._FileStorage__objects[expected_key]),
            str(self.base_model)
        )

<<<<<<< HEAD
    def test_save_creates_file_with_correct_data(self):
        self.storage.new(self.base_model)
        self.storage.save()
        with open(self.file_path, "r") as file:
            data = json.load(file)
            expected_data = {
                f"BaseModel.{self.base_model.id}": self.base_model.to_dict()
            }
            self.assertEqual(data, expected_data)

    def test_reload_loads_data_from_file(self):
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.new(BaseModel())
        self.storage.reload()
        self.assertEqual(
            self.storage._FileStorage__objects,
            {f"BaseModel.{self.base_model.id}": self.base_model}
        )

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

=======
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
         
    
>>>>>>> 80145c61fb0c9f412ac438c4bbbc6a8dbd5501d1
if __name__ == '__main__':
    unittest.main()
