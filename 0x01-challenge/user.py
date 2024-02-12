#!/usr/bin/python3
"""
This module contains a class called User
"""


class User:
    """ User class """

    def __init__(self):
        """ Init method """

        self.__email = None

    @property
    def email(self):
        """ This is a getter for email  """

        return self.__email

    @email.setter
    def email(self, value):
        """ This is a setter for email  """

        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
