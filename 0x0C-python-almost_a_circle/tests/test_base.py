#!/usr/bin/python3
""" Unit tests for 1) models/base.py """

from models.base import Base
# from models.Rectangle import Rectangle
import unittest


class Test_Base(unittest.TestCase):

    def setUP(self):
        """ ??? """
        pass

    def tearDown(self):
        """ yooo """
        pass

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(Base.__doc__)

    def test_simple(self):
        """ simplest test cases """
        bae = Base(1)
        self.assertEqual(1, bae.id)
        self.assertNotEqual(99, bae.id)
        bae = Base(99)
        self.assertEqual(bae.id, 99)

    def test_InputErrors(self):
        """ tests for input error """
        with self.assertRaises(AttributeError):
            self.assertIsEqual(bae(), 1)

    def test_empty(self):
        """ test empty conditions """
        bae = Base()
        self.assertEqual(1, bae.id)
        bae = Base(None)
        self.assertEqual(2, bae.id)
        bae = Base(None)
        self.assertEqual(3, bae.id)
        bae = Base(7)
        self.assertEqual(7, bae.id)

    def test_string(self):
        """ tests strings """
        bae = Base(2)
        self.assertEqual(2, bae.id)
        bae = Base("2")
        self.assertEqual('2', bae.id)

    def test_float(self):
        """ test floats """
        bae = Base(3)
        self.assertEqual(3, bae.id)
        bae = Base(3.45)
        self.assertEqual(3.45, bae.id)
        bae = Base(-4.56)
        self.assertEqual(-4.56, bae.id)

    def test_weird(self):
        """ test wtf things """
        bae = Base(4)
        self.assertEqual(4, bae.id)
        bae = Base([1, 2])
        self.assertEqual([1, 2], bae.id)
        bae = Base([1, "2"])
        self.assertEqual([1, '2'], bae.id)
        bae = Base([1, [1, 2]])
        self.assertEqual([1, [1, 2]], bae.id)
        bae = Base({"needle": 2})
        self.assertEqual({"needle": 2}, bae.id)
        bae = Base((1, 2))
        self.assertEqual((1, 2), bae.id)
        bae = Base(1)
        self.assertEqual(1, bae.id)
        bae = Base()
        self.assertEqual(6, bae.id)

    def test_moreErrors(self):
        """ more error checking """
        # with self.assertRaises(SyntaxError):
        # bae = base ( , )
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('NaN'))
        self.assertNotEqual(float('NaN'), bae.id)
        with self.assertRaises(ValueError):
            bae = Base(float('bob'))
        with self.assertRaises(ValueError):
            bae = Base(int('poop'))
        bae = Base()
        self.assertEqual(4, bae.id)

        # testing something
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        bae = Base(float('inf'))
        self.assertEqual(float('inf'), bae.id)
        # done with testing

        bae = Base()
        self.assertEqual(5, bae.id)

        def test_id(self):
            """ tests the if id works properly """
            poop = Base()
            poopID = poop.id
            poop2 = Base(69)
            poop3 = Base(100)
            poop4 = Base()
            self.assertTrue(poopID, 1)
            self.assertEqual(poopID, 1)
            self.assertFalse(poopID, poop4.id)
            self.assertTrue(poopID + 1, poop4.id)
            self.assertFalse(poop2, poop3)
            seld.assertEqual(poop3.id, 100)

        def test_class(self):
            """ tests subclass """
            poop = Base()
            self.assertTrue(issubclass(type(poop), Base))

        def test_to_json_string(self):
            """ tests if this method works """
            # test1 = Rectangle(1, 1, 1, 1, 1)
            """ nvm cant call child from inside parent. """
            pass

if __name__ == "__main__":
    unittest.main()
