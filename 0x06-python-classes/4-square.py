#!/usr/bin/python3
"""class Square defined"""


class Square:
    """Represents a square
    Attributes:
        __size (int): side square size
    """
    def __init__(self, size=0):
        """square initialization
        Args:
            size (int): side square size
        Returns:
            None
        """
        self.size = size

    def area(self):
        """square's area calculation
        Returns:
            square area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
