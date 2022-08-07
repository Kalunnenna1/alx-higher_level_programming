#!/usr/bin/python3
""" unittest for models/SQUARE.py
I AM LITERALLY COPY PASTING THIS FROM RECTANGLES
AND JUST CHANGING ALL 5 ARGUMENTS TO JUST 4
AND CHANGING ALL RECT TO SUQRES...
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import sys
from io import StringIO


class Test_Square(unittest.TestCase):

    def setUp(self):
        """ ??? """
        pass

    def tearDown(self):
        """ maplestory """
        pass

    def test_docstring(self):
        """ check to see if present """
        self.assertIsNotNone(Square.__doc__)

    def test_simple(self):
        """ simple basic tests """
        poop1 = Square(1)
        poop2 = Square(2)
        poop3 = Square(3)
        self.assertTrue(poop1.id, 1)
        self.assertEqual(poop2.size, poop2.size)
        self.assertNotEqual(poop1.id, poop2.id)
        self.assertEqual(poop1.size, 1)
        self.assertEqual(poop1.size, 1)
        self.assertEqual(poop2.size, 2)
        self.assertEqual(poop3.x, 0)
        poopFancy = Square(4, 5, 6, 7)
        self.assertEqual(poopFancy.id, 7)
        self.assertEqual(poopFancy.size, 4)
        self.assertEqual(poopFancy.size, 4)
        self.assertEqual(poopFancy.x, 5)
        self.assertEqual(poopFancy.y, 6)

    def test_syntaxErrors(self):
        """ tests the syntax of no or 1 argument """
        with self.assertRaises(TypeError):
            test = Square()
            test2 = Square(1)
            test3 = Square(None)
            test4 = Square([1])
            test5 = Square([])

    def test_int_validator(self):
        """ tests the integer validator method """
        with self.assertRaises(TypeError):
            test1 = Square("a")
            test2 = Square([2])
            test3 = Square({"3": 4})
        with self.assertRaises(ValueError):
            test1 = Square(-1)
            test2 = Square(0)
            test3 = Square(1, 2, 0, -3)
            test4 = Square(9, -9, 1, 2)

    def test_area(self):
        """ tests the area method """
        test1 = Square(1, 1, 1, 1)
        self.assertEqual(test1.area(), 1)
        with self.assertRaises(TypeError):
            test2 = test1.area(1)

    def test_display(self):
        """ wtf do i do for this method """
        sys.stdout = StringIO()
        test1 = Square(2, 2, 2)
        test1.display()
        self.assertEqual("\n\n  ##\n  ##\n", sys.stdout.getvalue())
        sys.stdout = sys.__stdout__

    def test_display2(self):
        """ wtf do i do for this method """
        sys.stdout = StringIO()
        test1 = Square(1, 1, 1)
        test1.display()
        self.assertEqual("\n #\n", sys.stdout.getvalue())
        sys.stdout = sys.__stdout__

    def test_string(self):
        """ tests the __str__ """
        test1 = Square(1, 1, 1, 1)
        self.assertEqual(str(test1), "[Square] (1) 1/1 - 1")

    def test_update_args(self):
        """ tests the update *args """
        test1 = Square(1, 1, 1, 1)
        self.assertEqual(test1.size, 1)
        self.assertEqual(test1.x, 1)
        test1.update(3, 3, 3, 3)
        self.assertEqual(test1.size, 3)
        self.assertEqual(test1.y, 3)
        self.assertEqual(test1.x, 3)
        self.assertEqual(test1.size, 3)
        self.assertEqual(test1.id, 3)

    def test_update_kwargs(self):
        """ tests the update with keywords """
        test1 = Square(1, 1, 1, 1)
        self.assertEqual(test1.size, 1)
        test1.update(id=3)
        self.assertEqual(test1.id, 3)
        self.assertEqual(test1.size, 1)
        test1.update(y=69)
        self.assertEqual(test1.y, 69)

    def test_update_errors(self):
        """ tests update errors, either Type or Value """
        test1 = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            test1.update('a', 1)
            test1.update(12, [12])
            test1.update({"poopy": 1}, 1)
            test1.update(None)
        with self.assertRaises(ValueError):
            test1.update(0, 0, 0, 0)
            test1.update(-1, -1, -1,)

    def test_to_dict(self):
        """ tests a string to a dict method """
        test1 = Square(1, 1, 1, 1)
        test2 = {'id': 1, 'size': 1, 'size': 1, 'x': 1, 'y': 1}
        test1DIC = test1.to_dictionary()
        self.assertEqual(test2, test1DIC)

    """ need to test json stuff in here """
    def test_to_json(self):
        """ tests the object converted to json string """
        test1 = Square(1, 1, 1, 1)
        test1DIC = test1.to_dictionary()
        test1STR = test1.to_json_string(test1DIC)
        self.assertTrue(test1STR, json.dumps(test1DIC))

    def test_save_to_file(self):
        """ tests if we saved to the file """
        test1 = Square(1, 1, 1, 1)
        test1DIX = [test1.to_dictionary()]
        Square.save_to_file([test1])
        with open("Square.json", mode='r', encoding='utf-8') as f:
            red = f.read()
            self.assertEqual(json.dumps(test1DIX), red)

    def test_from_json(self):
        """ from a json string to object """
        test1 = Square(1, 1, 1, 1)
        test1DIX = [test1.to_dictionary()]
        test2 = Square.to_json_string(test1DIX)
        self.assertTrue(test2, json.dumps(test1DIX))
        test3 = Square.from_json_string(test2)
        self.assertTrue(test2, test3)
        # self.assertEqual(test2, test3) fails cause " and '

    def test_create(self):
        """ create tests """
        test1 = Square(1, 1, 1, 1)
        test1DICT = test1.to_dictionary()
        test2 = Square.create(**test1DICT)
        test1S = {'x': 1, 'size': 1, 'y': 1, 'id': 1, 'size': 1}
        test2S = {'x': 1, 'size': 1, 'y': 1, 'id': 1, 'size': 1}
        self.assertEqual(test1DICT, test1S)
        self.assertTrue(test2, test2S)
        self.assertFalse(test1 is test2)
        self.assertTrue(test1S is not test2S)

    def test_load(self):
        """ testing the load from ciles class method """
        test1 = Square(1, 1, 1, 1)
        # object of type square has no length error. need to put in list
        test1LIST = [test1]
        Square.save_to_file(test1LIST)
        x = Square.load_from_file()
        self.assertTrue(isinstance(x, list))
        self.assertTrue(isinstance(x[0], Square))

    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """
    """ POST CHECKER """

    def test_checker(self):
        """ testing basic shit """
        test1 = Square(1)
        self.assertTrue(test1)
        test2 = Square(1, 2)
        self.assertTrue(test2)
        test3 = Square(1, 2, 3)
        self.assertTrue(test3)

    def test_checker2(self):
        """testing the errors"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            test4 = Square("1", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            test5 = Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            test6 = Square(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            test8 = Square(-1)
            test13 = Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            test9 = Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            test12 = Square(1, 2, -3)

    def test_display3(self):
        """ wtf do i do for this method """
        sys.stdout = StringIO()
        test1 = Square(2)
        test1.display()
        self.assertEqual("##\n##\n", sys.stdout.getvalue())
        sys.stdout = sys.__stdout__

    def test_display4(self):
        """ wtf do i do for this method """
        sys.stdout = StringIO()
        test1 = Square(2, 2)
        test1.display()
        self.assertEqual("  ##\n  ##\n", sys.stdout.getvalue())
        sys.stdout = sys.__stdout__

    def test_checker3(self):
        """ checks none for save to file error """
        test1 = Square.save_to_file(None)
        self.assertEqual(test1, None)
        test2 = Square.save_to_file([])
        self.assertEqual(test2, None)

    def test_sumin(self):
        """ omg i have to test if it woprks """
        Square.save_to_file(None)
        with open("Rectangle.json", mode="r", encoding='utf-8') as f:
            l = f.read()
        l2 = "[]"
        self.assertEqual(l, l2)

    def test_sumin1(self):
        """ omg i have to test if it woprks """
        Square.save_to_file([])
        with open("Rectangle.json", mode="r", encoding='utf-8') as f:
            l = f.read()
        l2 = '[]'
        self.assertEqual(l, l2)

if __name__ == "__main__":
    unittest.main()
