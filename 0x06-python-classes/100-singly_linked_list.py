#!/usr/bin/python3

"""" reprsenting a Node of singly linked list"""


class Node:
    """defing a node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """"get or set the data of singly linked list"""
            return self.__data

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """set or get next node of singly linked list"""
            return self.__next_node

        @next_node.setter
        def next_nod(self, value):
            if (not isinstance(value, Node)) or value is not None:
                raise TypeError("next_node must be a node object")
            self.__next_node = value

    """ reprsenting the singly liked part """


class SinglyLinkedList:
    """defing a siglylinked list class"""

    def __init__(self):
        """ initlizing only the head intance for good
         Args:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """inset value according to the sortation of the singly linked list
            Args:
                value (int): the value to be compred and inserted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node

        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None) and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """ helps to print the data of the singly linke lisst"""
        v = []
        temp = self.__head
        while temp is not None:
            v.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(v))
