# Step 1: Triangle ki teen sides ko input karen
side1 = int(input("Pehli side daaliye: "))
side2 = int(input("Dusri side daaliye: "))
side3 = int(input("Teesri side daaliye: "))

# Step 2: Triangle type check karen
if side1 == side2 == side3:
    print("Ye Equilateral triangle hai.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Ye Isosceles triangle hai.")
else:
    print("Ye Scalene triangle hai.")
