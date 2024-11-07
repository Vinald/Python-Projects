# A function to solve a q.e of the form ax2 + bx + c = 0
import math
import cmath


def equation():
    a = int(input("Enter the coefficient in x2, a: "))
    b = int(input("Enter the coefficient in x, b: "))
    c = int(input("Enter the coefficientless in x , c: "))
    d = b * b - 4 * a * c
    if d < 0:
        print("Has complex roots")
        root1 = (-b / (2 * a)) + cmath.sqrt(d) / (2 * a)
        root2 = (-b / (2 * a)) - cmath.sqrt(d) / (2 * a)
        print("Roots = ", root1, ",", root2)
    elif d == 0:
        print("Has equal and definite roots")
        roots = root1 = root2 = -b / (2 * a)
        print("Roots = ", roots)
    else:
        print("Has definite and different roots")
        root1 = (-b / (2 * a)) + math.sqrt(abs(d)) / (2 * a)
        root2 = (-b / (2 * a)) - math.sqrt(abs(d)) / (2 * a)
        print(f'(Roots = , {root1}, {root2})')


equation()
