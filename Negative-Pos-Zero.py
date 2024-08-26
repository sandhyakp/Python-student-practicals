# Step 1: Number ko input karen
num = float(input("Koi bhi number daaliye: "))

# Step 2: Positive, negative ya zero check karen
if num > 0:
    print(num, "positive number hai.")
elif num < 0:
    print(num, "negative number hai.")
else:
    print(num, "zero hai.")
