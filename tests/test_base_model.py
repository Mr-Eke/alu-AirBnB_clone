import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """ Test case for the BaseModel class in the 'models' module."""

    def setUp(self):
        """Set up the initial state for the tests."""
        self.obj_1 = BaseModel()
        self.obj_2 = BaseModel()

    def tearDown(self):
        """Clean up resources after each test."""
        del self.obj_1
        del self.obj_2

    def test_instantiation(self):
        """Test if BaseModel objects are instantiated correctly."""
        self.assertIsInstance(self.obj_1, BaseModel)

    def test_attr_type(self):
        """Test the data types of specific attributes of BaseModel objects."""
        with self.subTest():
            self.assertIsInstance(self.obj_1.id, str)
        with self.subTest():
            self.assertIsInstance(self.obj_1.updated_at, datetime)

    def test_unique_id(self):
        """ Test if the id attribute of different
        BaseModel instances is unique.
        """
        self.assertNotEqual(self.obj_1.id, self.obj_2.id)

    def test_id_assignment(self):
        """ validate that The id attribute of the BaseModel object is a
        valid UUID.
        """
        self.assertTrue(uuid.UUID(self.obj_1.id, version=4))






