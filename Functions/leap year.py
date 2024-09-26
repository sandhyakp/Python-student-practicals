def leap(year):
    if year %4==0 and year %100!= 0 or year %400 ==0:
        return "Leap Year"
    else:
        return "not a leap year"


year = int(input("Enter the Year to find out Leap Year or not "))

x = leap(year)    
print(x)
