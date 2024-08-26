# Step 1: Input the numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Step 2: Use a third variable to swap the values
temp = a  # Save the value of 'a' in 'temp'
a = b     # Assign the value of 'b' to 'a'
b = temp
# Assign the value of 'temp' (which is the original value of 'a') to 'b'

# Step 3: Print the swapped values
print("After swapping, the value of a is:", a)
print("After swapping, the value of b is:", b)
