import math as mt


a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

d = b*b-4*a*c

if (d<0):
    print('Нет действиетельных корней')
elif (d==0):
    print('x = ' -b/(2*a))
else:
    x1 = (-b + mt.sqrt(d)) / (2 * a)
    x2 = (-b - mt.sqrt(d)) / (2 * a)
    print('x1 = ',x1,'x2 = ', x2)

