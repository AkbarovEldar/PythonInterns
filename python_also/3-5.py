import math as mt


x = float(input('Введите x: '))
if x >= - mt.pi and x<= mt.pi :          
    res = float(mt.cos(3*x))
    print('y = cos(3x) = ', res)
else:
    print('y = x = ', x)

