from math import sqrt


class Person:
    def __init__(self):
        self.__age = 0
        self.__name = "No name"


    @property
    def age(self):
        print("Это геттер")
        return self.__age

    @age.setter
    def age(self, a):
        print("Это сеттер")
        self.__age = a

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, a):
        self.__name = a



class Animal:
    def bark(self):
        print("bark")

def func1(a):
    a = a
    print("func1!!!! " + a)

def func2(a):
    a = str(a)
    print("func2!!!! " + a)


def sqrt2(a):
    return sqrt(a)