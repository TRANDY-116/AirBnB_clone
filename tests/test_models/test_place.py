#!/usr/bin/python3
"""Unittest for Place Class."""

import unittest
from datetime import datetime
from models.place import Place
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for Plave class."""

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
        """Tests initialization of Place class."""

        i = Place()
        self.assertEqual(str(type(i)), "<class 'models.place.Place'>")
        self.assertIsInstance(i, Place)
        self.assertTrue(issubclass(type(i), BaseModel))

    def test_8_attributes(self):
        """Testing attributes of Place class."""
        attributes = storage.attributes()["Place"]
        j = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(j, k))
            self.assertEqual(type(getattr(j, k, None)), v)


if __name__ == "__main__":
    unittest.main()