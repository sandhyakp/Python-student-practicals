def check_number():
    number = float(input("Enter number: "))
    
    if number > 0:
        print(f"{number} is Positive")
    elif number < 0:
        print(f"{number} is Negative")
    else:
        print("number is Zero")

check_number()
