#!/usr/bin/python3
"""Unittest for City Class."""

import unittest
from datetime import datetime
from models.city import City
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reseting FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests initialization of City class."""

        i = City()
        self.assertEqual(str(type(i)), "<class 'models.city.City'>")
        self.assertIsInstance(i, City)
        self.assertTrue(issubclass(type(i), BaseModel))

    def test_8_attributes(self):
        """Testing attributes of CIty class."""
        attributes = storage.attributes()["CIty"]
        j = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(j, k))
            self.assertEqual(type(getattr(j, k, None)), v)


if __name__ == "__main__":
    unittest.main()