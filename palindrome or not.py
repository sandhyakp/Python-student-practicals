# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Original number ko store karen
original = n

# Step 3: Reverse number ko calculate karen
reverse = 0
while n > 0:
    digit = n % 10  # Last digit nikalte hain
    reverse = reverse * 10 + digit  # Reverse ko update karte hain
    n = n // 10  # Last digit remove karte hain

# Step 4: Check karen original number aur reverse number equal hain ya nahi
if original == reverse:
    print(original, "ek palindrome number hai.")
else:
    print(original, "ek palindrome number nahi hai.")
