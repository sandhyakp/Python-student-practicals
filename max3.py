# Step 1: Teen numbers ko input karen
num1 = int(input("Pehla number daaliye: "))
num2 = int(input("Dusra number daaliye: "))
num3 = int(input("Teesra number daaliye: "))

# Step 2: Maximum check karen
if num1 > num2 and num1 > num3:
    print("Maximum number hai:", num1)
elif num2 > num3:
    print("Maximum number hai:", num2)
else:
    print("Maximum number hai:", num3)
