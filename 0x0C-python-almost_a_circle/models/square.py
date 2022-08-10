#!/usr/bin/python3
"""A Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """update string representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"


    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    
    def update(self, *args, **kwargs):
        """update attributes"""
        if args != None and len(args) != 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dictionary(self):
        """return the dictionary representation of a Square"""
        dict_rep = {}
        dict_rep['x'] = self.x
        dict_rep['y'] = self.y
        dict_rep['id'] = self.id
        dict_rep['size'] = self.width
        return dict_rep
