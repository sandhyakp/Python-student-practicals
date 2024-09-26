def marks():
    elements = int(input("Enter the Total subjects :"))
    print("Enter the subjects marks one by one")
    
    Science = int(input("Enter the marks for Science "))
    English = int(input("Enter the marks for English "))
    Hindi = int(input("Enter the marks for Hindi "))
    Maths = int(input("Enter the marks for Maths "))
    Japanese = int(input("Enter the marks for Japanese "))
    
    total =  Science + English + Hindi + Maths + Japanese
    average = total/5
    
    return total,average

total,average = marks()
print(f"total marks {total}\n Average of Marks {average}")
