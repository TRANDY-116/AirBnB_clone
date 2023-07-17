#!/usr/bin/python3
"""Unittest for Review Class."""

import unittest
from datetime import datetime
from models.review import Review
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for Review class."""

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
        """Tests initialization of Review class."""

        i = Review()
        self.assertEqual(str(type(i)), "<class 'models.review.Review'>")
        self.assertIsInstance(i, Review)
        self.assertTrue(issubclass(type(i), BaseModel))

    def test_8_attributes(self):
        """Testing attributes of CIty class."""
        attributes = storage.attributes()["Review"]
        j = Review()
        for a, b in attributes.items():
            self.assertTrue(hasattr(j, a))
            self.assertEqual(type(getattr(j, a, None)), b)


if __name__ == "__main__":
    unittest.main()