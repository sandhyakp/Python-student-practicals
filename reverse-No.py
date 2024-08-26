# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Reverse number ko initialize karen
reverse = 0

# Step 3: Loop tab tak chale jab tak number 0 nahi ho jaata
while n > 0:
    digit = n % 10  # Last digit nikalte hain
    reverse = reverse * 10 + digit  # Reverse ko update karte hain
    n = n // 10  # Last digit remove karte hain

# Step 4: Reverse number ko print karen
print("Number ka reverse hai:", reverse)
