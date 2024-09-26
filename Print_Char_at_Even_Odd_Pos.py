'''give_string = input("Enter the String :")
len = 0

if x in give_string:
    give_string //2
    print("Even")
    
else:
    print("odd")'''
give_string = input("Enter the String: ")

# Checking if the length of the string is even or odd
length = len(give_string)

if length % 2 == 0:
    print("Even")
else:
    print("Odd")
