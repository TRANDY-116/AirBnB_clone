#!/usr/bin/python3
"""
    Module for FileStorage
"""

import json, os


class FileStorage:
    """ 
        Class that serializes instances to json file and deserializes json files to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            To return the dictionary objects
        """
        return self.__objects
    
    def new(self, obj):
        """
           sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        d = {}
        for key, obj in self.__objects.items():
            d[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(d, file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                d = json.load(file)
                for key, score in d.items():
                    class_name, obj_id = key.split('.')
                    class_obj = getattr(__import__(class_name), class_name)
                    obj = class_obj(**score)
                    self.__objects[key] = obj