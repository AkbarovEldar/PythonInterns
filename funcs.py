from math import sqrt


class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        print("Это геттер")
        return self.__age

    @age.setter
    def age(self, a):
        print("Это сеттер")
        self.__age = a





def func1(a):
    a = a
    print("func1!!!! " + a)

def func2(a):
    a = str(a)
    print("func2!!!! " + a)


def sqrt2(a):
    return sqrt(a)