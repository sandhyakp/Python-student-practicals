# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Sum ko initialize karen
sum = 0

# Step 3: Loop tab tak chale jab tak number 0 nahi ho jaata
while n > 0:
    digit = n % 10  # Last digit nikalte hain
    sum += digit  # Sum mein add karte hain
    n = n // 10  # Last digit remove karte hain

# Step 4: Sum ko print karen
print("Digits ka sum hai:", sum)
