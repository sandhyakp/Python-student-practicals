num = int(input("Enter the Year to find Out Leap Year or Not: "))
if num %4 == 0 and num % 100!= 0 or num %400 == 0:
    print(f"These is leap year:",{num})
else:
    print(f"These is Not a leap year:",{num}) 
