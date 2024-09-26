def triangle():
    side1 = float(input("1 side of the triangle: "))
    side2 = float(input("2 side of the triangle: "))
    side3 = float(input("3 side of the triangle: "))
    
    if side1 == side2 == side3:
        print("These is Equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("These is Isosceles")
    else:
        print("These is Scalene")

triangle()
