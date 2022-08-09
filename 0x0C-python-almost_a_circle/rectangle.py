#!/usr/bin/python3
"""Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """create a rectangle class inheriting from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """demension of Rectangle
        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x:
            y:
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """get x co-ordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x-coordinate"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """get y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y-coordinate"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """ returns the area value of the Rectangle instance"""
        return self.__width * self.height


    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x, end="")
            for col in range(self.width):
                if col is self.width - 1:
                    print("#", end="\n")
                else:
                    print("#", end="")


    def __str__(self):
        """return representation for the Rectangle Object"""
        start = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        end = f"{self.width}/{self.height}"
        return start + end


    def update(self, *args, **kwargs):
        if args != None and len(args) != 0:
            atrs = ['id', 'width', 'height', 'x', 'y']
            for atr in range(len(args)):
                setattr(self, atrs[atr], args[atr])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dictionary(self):
        """return the dictionary representation of a Rectangle"""
        dict_rep = {}
        dict_rep['x'] = self.x
        dict_rep['y'] = self.y
        dict_rep['id'] = self.id
        dict_rep['height'] = self.height
        dict_rep['width'] = self.width
        return dict_rep
