#!/usr/bin/python3

""" init the base class base of all other class """
import json

""" the abse calls is starting here """


class Base:
    """ the base created here """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initing a calss base object
        Args:
            id(int) - the unique number to the object
        """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(str(cls.__name__) + ".json", "w") as file:
            if (list_objs is None or len(list_objs) == 0):
                file.write("[]")
            else:
                list_obj = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_obj))

    def from_json_string(json_string):
        """that returns the list of the JSON string
        representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(str(cls.__name__) + ".json", "r") as file:
                tom = file.read()
                tom = Base.from_json_string(tom)
                return [cls.create(**obj) for obj in tom]
        except IOError:
            return []
