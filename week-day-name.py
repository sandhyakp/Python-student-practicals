# Step 1: Week number ko input karen
week_num = int(input("Week number (1-7) daaliye: "))

# Step 2: Week day ko print karen
if week_num == 1:
    print("Monday")
elif week_num == 2:
    print("Tuesday")
elif week_num == 3:
    print("Wednesday")
elif week_num == 4:
    print("Thursday")
elif week_num == 5:
    print("Friday")
elif week_num == 6:
    print("Saturday")
elif week_num == 7:
    print("Sunday")
else:
    print("Invalid week number!")
