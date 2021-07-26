import math as mt

ang = int(input())

if ang == 30:
    s = float(mt.sin(mt.radians(ang)))
    c = float(mt.cos(mt.radians(ang)))
    print('sin угла 30 гр. равен ', s)
    print('cos угла 30 гр. равен', c)
