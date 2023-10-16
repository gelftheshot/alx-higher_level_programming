#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base
import random
import io
import sys

class Test_rectangle_general(unittest.TestCase):

    def test_is_it_Base(self):
        r1 = Rectangle(1, 2)
        t = isinstance(r1, Base)
        self.assertTrue(t)

    def test_empty_case(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_case(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_two_case(self):

        r1 = Rectangle(2,3)
        r2 = Rectangle(1,2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.y, 0)
    def test_three_case(self):

        r1 = Rectangle(1,2,5)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)

    def test_four_case(self):
        
        r1 = Rectangle(1, 3, 4, 5)
        self.assertEqual(1, r1.width)
        self.assertEqual(3, r1.height)
        self.assertEqual(4, r1.x)
        self.assertEqual(5, r1.y)

    def test_five_case(self):

        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(1, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(3, r1.x)
        self.assertEqual(4, r1.y)
        self.assertEqual(5, r1.id)
    
    def test_six_case(self):

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

class Test_getter_setter(unittest.TestCase):


    def test_width_getter(self):
        r = Rectangle(1,2,3,4,5)
        self.assertEqual(r.width, 1)

    def test_width_getter_private(self):
        r = Rectangle(1,2,3,4,5)
        with self.assertRaises(AttributeError):
            print(r.__width)
    def test_width_setter(self):
        r = Rectangle(1,2,3,4,5)
        r.width = 10
        self.assertEqual(10, r.width)
    
    def test_height_getter(self):
        r = Rectangle(1,2,3,4,5)
        self.assertEqual(2, r.height)
    
    def test_height_getter_private(self):
        r = Rectangle(1,2,3,4,5)
        with self.assertRaises(AttributeError):
            print(r.__height)
    def test_height_setter_private(self):
        r = Rectangle(1,2,3,4,5)
        r.height = 10
        self.assertEqual(10, r.height)
    def test_x_getter(self):
        r = Rectangle(1,2,3,4,5)
        self.assertEqual(r.x, 3)
    def test_x_getter_private(self):
        r = Rectangle(1,2,3,4,5)
        with self.assertRaises(AttributeError):
            print(r.__x)
    def test_x_setter(self):
        r = Rectangle(1,2,3,4,5)
        r.x =10
        self.assertEqual(10, r.x)
    def test_y_getter(self):
        r = Rectangle(1,2,3,4,5)
        self.assertEqual(4, r.y)
    def test_y_getter_private(self):
        r = Rectangle(1,2,3,4,5)
        with self.assertRaises(AttributeError):
            print(r.__y)
    def test_y_setter(self):
        r = Rectangle(1,2,3,4,5)
        r.y = 10
        self.assertEqual(10, r.y)
class test_width_validater_test(unittest.TestCase):
    
    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 2)
    def test_width_zero(self):
         with self.assertRaisesRegex(ValueError, "width must be > 0"):
             r = Rectangle(0, 1)
    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(1.4, 6)
    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("4", 7)
    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([1, 2, 3], 6)
    def test_width_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({"tom" : 5, "baba": 6}, 9)
    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({1,2,3}, 4)
    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((1, 3, 4), 5)
    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 5)
    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, None)

class test_height_validator(unittest.TestCase):
    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(2, -2)
    def test_height_zero(self):
         with self.assertRaisesRegex(ValueError, "height must be > 0"):
             r = Rectangle(1, 0)
    def test_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(5, None)
    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(4, 6.7)
    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(4, "7")
    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(6, [1, 2, 3])
    def test_height_dictionary(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(9, {"tom" : 5, "baba": 6})
    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(4, {1,2,3})
    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(5, (1, 3, 4))
    def test_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(5, True)

class test_x_validater(unittest.TestCase):

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -7)
    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, None)
    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, 4.3)
    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, "otme")
    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, [2, 3, 4,])
    def test_x_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, {'tata' : 3, "haaha": 6})
    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, {1, 2, 3})
    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, (1, 2, 4))
    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, True)

class test_y_validater(unittest.TestCase):

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 2, 3, -9)
    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, None)
    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, 6.5)
    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, "gelf")
    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, [1,2,3])
    def test_y_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, {"67" : 5, "yup" : 7})
    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, {1, 2, 6})
    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, (1, 2, 3))
    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, True)

class Test_area(unittest.TestCase):

    def test_area_normal(self):
        r = Rectangle(3, 2)
        self.assertEqual(6, r.area())
    
    def test_area_large(self):
        r = Rectangle(87893884844, 8229454443)
        self.assertEqual(87893884844 * 8229454443, r.area())
    
    def test_area_random(self):
        x = random.randint(1, 100000000000)
        y = random.randint(1, 100000000000)
        r = Rectangle(x, y)
        self.assertEqual(x * y, r.area())
        
    def test_area_changed(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 7
        r.height = 7
        self.assertEqual(49, r.area())

class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)
class Test_update_args(unittest.TestCase):

    def test_only_args(self):
        r = Rectangle(1,2)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [10, 20, 30, 40, 50])
    def test_empty_case(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update()
        self.assertEqual([r.width, r.height, r.x, r.y, r.id], [10, 20, 30, 40, 50])
    def test_firt_is_id(self):
        r  = Rectangle(10, 20, 30, 40)
        r.update(1)
        self.assertEqual([10, 20, 30, 40, 1], [r.width, r.height, r.x, r.y, r.id])
    def test_second_width(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 2)
        self.assertEqual([2, 20, 30, 40, 1], [r.width, r.height, r.x, r.y, r.id])
    def test_thired_height(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 2, 3)
        self.assertEqual([1, 2, 3, 30, 40], [r.id, r.width, r.height, r.x, r.y])
    def test_fourth_x(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 2, 3, 4)
        self.assertEqual([1, 2, 3, 4, 40], [r.id, r.width, r.height, r.x, r.y])
    def test_fifth_y(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual([1, 2, 3, 4, 5], [r.id, r.width, r.height, r.x, r.y])
    
class Test_update_kargs(unittest.TestCase):

    def test_only_kargs(self):
        r = Rectangle(1,2)
        r.update(id = 10, width = 20, height = 30, x = 40, y = 50)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [10, 20, 30, 40, 50])
    def test_empty_case(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update()
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [50, 10, 20, 30, 40])
    def test_id(self):
        r  = Rectangle(10, 20, 30, 40)
        r.update(id = 1)
        self.assertEqual([1, 10, 20, 30, 40], [r.id, r.width, r.height, r.x, r.y])
    def test_width(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(id = 1, width = 2)
        self.assertEqual([1, 2, 20, 30, 40], [r.id, r.width, r.height, r.x, r.y])
    def test_height(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(id = 1, width = 2, height = 3)
        self.assertEqual([1, 2, 3, 30, 40], [r.id, r.width, r.height, r.x, r.y])
    def test_x(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(id = 1, width = 2, height = 3, x = 4)
        self.assertEqual([1, 2, 3, 4, 40], [r.id, r.width, r.height, r.x, r.y])
    def test_y(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(id = 1, width = 2, height = 3, x = 4, y = 5)
        self.assertEqual([1, 2, 3, 4, 5], [r.id, r.width, r.height, r.x, r.y])
    def test_in_random_order(self):
         r  = Rectangle(10, 20, 30, 40, 50)
         r.update(height = 9, y = 88, x = 49)
         self.assertEqual([50, 10, 9, 49, 88], [r.id, r.width, r.height, r.x, r.y])
    def test_update_non_attribute_value(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(tom = 88, gelf = 98)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [50, 10, 20, 30, 40])
    def test_update_non_attribute_value_and_attribue_value(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(tom = 88, gelf = 98, id = 1, c = 99, y = 5)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [1, 10, 20, 30, 5])
    def test_both_args_and_kargs(self):
        r  = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 3, 4, y = 0, x = 54)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [1, 3, 4, 30, 40])

class TestRectangle_to_dictionary(unittest.TestCase):
    """testing method to dictionary."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()