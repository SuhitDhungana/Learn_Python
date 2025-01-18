def main():
    import math
    r = float(input("What's the radius of the circle? "))
    perimeter = round(2 * math.pi * r, 2)
    area = math.pi * pow(r, 2)
    print(f"The perimter of the circle is {perimeter}, and the area of the circle is {round(area, 2)}")
    a = float(input("What's one side of the triangle? "))
    b = float(input("What's another side of the triangle? "))
    h = math.sqrt(pow(a, 2) + pow(b, 2))
    print(f"The hypotenuse of the triangle is: {round(h,2)}")
main()