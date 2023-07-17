#!/usr/bin/python3
"""Unittest for State Class."""

import unittest
from datetime import datetime
from models.state import State
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for State class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tear down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reseting FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests initialization of State class."""

        i = State()
        self.assertEqual(str(type(i)), "<class 'models.state.State'>")
        self.assertIsInstance(i, State)
        self.assertTrue(issubclass(type(i), BaseModel))

    def test_8_attributes(self):
        """Testing attributes of State class."""
        attributes = storage.attributes()["State"]
        j = State()
        for a, b in attributes.items():
            self.assertTrue(hasattr(j, a))
            self.assertEqual(type(getattr(j, a, None)), b)


if __name__ == "__main__":
    unittest.main()