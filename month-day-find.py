# Step 1: Month number ko input karen
month_num = int(input("Month number (1-12) daaliye: "))

# Step 2: Days ko print karen
if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
    print("31 days")
elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
    print("30 days")
elif month_num == 2:
    print("28 ya 29 days (leap year par depend karta hai)")
else:
    print("Invalid month number!")
