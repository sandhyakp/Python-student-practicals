# Step 1: Days ko input karen
days = int(input("Kitne din hain daaliye: "))

# Step 2: Years calculate karen
years = days // 365

# Step 3: Remaining days nikal kar months calculate karen
remaining_days = days % 365
months = remaining_days // 30

# Step 4: Baaki ke days calculate karen
remaining_days = remaining_days % 30

# Step 5: Results print karen
print("Years:", years)
print("Months:", months)
print("Remaining Days:", remaining_days)
