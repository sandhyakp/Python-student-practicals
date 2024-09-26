
def week_day():
    week_number = int(input("Enter a week day : "))
    
    week_days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    
    if 1 <= week_number <= 7:
        print(f"Day {week_number} is {week_days[week_number]}")
    else:
        print("Invalid week number. Please enter a number between 1 and 7.")

week_day()
