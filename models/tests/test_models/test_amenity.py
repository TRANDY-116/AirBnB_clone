#!/usr/bin/python3
"""Unittest for Amenity Class."""

import unittest
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests initialization of Amenity class."""

        i = Amenity()
        self.assertEqual(str(type(i)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(i, Amenity)
        self.assertTrue(issubclass(type(i), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        j = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(j, k))
            self.assertEqual(type(getattr(j, k, None)), v)


if __name__ == "__main__":
    unittest.main()