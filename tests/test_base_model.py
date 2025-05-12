import unittest
from models.base_model import BaseModel
import uuid

class TestBaseModel(unittest.TestCase):
    """ Test cases for the base model class and its attributes"""

    def setUp(self):
        self.base_model_obj = BaseModel()
        self.id_str_obj = self.base_model_obj.id

    def test_obj_initialization(self):
        self.assertTrue(isinstance(self.base_model_obj, BaseModel))

    def test_attributes(self):
        """ tests all attributes of basemodel"""
        id_uuid_obj = uuid.UUID(self.id_str_obj)

        self.assertIsInstance(id_uuid_obj, uuid.UUID)
        self.assertIsInstance(self.id_str_obj, str)
        





