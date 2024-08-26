# Step 1: Cost price aur selling price ko input karen
cp = float(input("Cost price daaliye: "))
sp = float(input("Selling price daaliye: "))

# Step 2: Profit ya loss check karen
if sp > cp:
    profit = sp - cp
    print("Profit hua:", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss hua:", loss)
else:
    print("Na profit, na loss.")
