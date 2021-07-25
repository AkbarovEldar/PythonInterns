a = float(input())
b = float(input())
o = str(input())


if (b == 0 and (o == "/" or o=="mod" or o=="div")):
    print("Деление на 0!")
elif (o == "+"):
    print(a+b)
elif (o == "-"):
    print(a - b)
elif (o == "/"):
    print(a / b)
elif (o == "*"):
    print(a * b)
elif (o == "mod"):
    print(a % b)
elif (o == "pow"):
    print(a ** b)
elif (o == "div"):
    print(a // b)

