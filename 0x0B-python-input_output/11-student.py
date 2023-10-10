#!/usr/bin/python3


"""defing a class student """


class Student():
    """ the class started here """

    def __init__(self, first_name, last_name, age):
        """ initing the insances of the class
        Args:
        first_name(str) - the first name of the student
        last_name(str) - the last name of the student
        age(int) - is the age of the sudent
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ rettuen the dic represtation of calss """
        if (isinstance(attrs, list)) and\
                (all(isinstance(li, str) for li in attrs)):
            new_dic = {}
            for ele in attrs:
                if hasattr(self, ele):
                    new_dic[ele] = self.__dict__[ele]
            return new_dic
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """ this will load the att of class from json
        Args:
            json - the dictionary represtation of json
        """

        for key, value in json.items():
            setattr(self, key, value)
