def month():
    month_number = int(input("Enter a month number (1-12): "))
    
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if 1 <= month_number <= 12:
        print(f"Month {month_number} has {days_in_month[month_number]} days")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")

month()
