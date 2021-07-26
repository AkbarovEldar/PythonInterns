import math as mt

a = int(input())

if a < 0:
    ang = int(input('Введите угол 60 гр.: '))
    c = float(mt.cos(mt.radians(ang)))          
    print('cos угла 60 гр. равен', round(c,3))
elif a > 0:
    ang = int(input('Введите угол 30 гр.: '))
    s = float(mt.sin(mt.radians(ang)))          
    print('sin угла 30 гр. равен', round(s,3))
