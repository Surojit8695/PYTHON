# 4. Write a Python program to solve the quadratic equation ax² + bx + c = 0 by getting input for coefficients
# from the user.
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Two distinct real roots are:")
    print("x1 =", x1)
    print("x2 =", x2)

elif d == 0:
    x = -b / (2*a)
    print("Two equal real roots are:")
    print("x1 = x2 =", x)

else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)

    print("Complex roots are:")
    print("x1 =", real, "+", imag, "i")
    print("x2 =", real, "-", imag, "i")