def num_3():
    num1 = float(input("first number: "))
    num2 = float(input("second number: "))
    num3 = float(input("third number: "))
    
    if num1 > num2 and num1 > num3:
        print(f"{num1} is max")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is max")
    else:
        print(f"{num3} is max")

num_3()
