def pl():
    cost_p = float(input("Enter the cost price: "))
    selling_p = float(input("Enter the selling price: "))
    
    if selling_p > cost_p:
        profit = selling_p - cost_p
        print(f"Profit: {profit}")
        
    elif cost_p > selling_p:
        loss = cost_p - selling_p
        print(f"Loss: {loss}")
    else:
        print("No Profit No Loss")

pl()
