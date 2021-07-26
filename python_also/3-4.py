import math as mt

print('Введите операцию: +, -, *, /, ^, sin, cos или tg')
oper = str(input())
if oper == '+':
    a = float(input('Введите число a: '))
    b = float(input('Введите число b: '))
    print(a, '+', b, '=', a+b)
elif oper == '-':
    a = float(input('Введите число a: '))
    b = float(input('Введите число b: '))
    print(a, '-', b, '=', a-b)
elif oper == '*':
    a = float(input('Введите число a: '))
    b = float(input('Введите число b: '))
    print(a, '*', b, '=', a*b)
elif oper == '/':
    a = float(input('Введите число a: '))
    b = float(input('Введите число b: '))
    print(a, '/', b, '=', a/b)
elif oper == '^':
    a = float(input('Введите основание'))
    b = float(input('Введите показатель степени'))
    print(a, '^', b, '=', a**b)
elif oper == 'sin':
    a = float(input('Введите число: '))
    res = float(mt.sin(a))
    print('sin угла', a, ' = ', res)
elif oper == 'cos':
    a = float(input('Введите число: '))
    res = float(mt.cos(a))
    print('sin угла', a, ' = ', res)
elif oper == 'tg':
    a = float(input('Введите число: '))
    res = float(mt.tan(a))
    print('sin угла', a, ' = ', res)
