# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Product ko initialize karen
product = 1

# Step 3: Loop tab tak chale jab tak number 0 nahi ho jaata
while n > 0:
    digit = n % 10  # Last digit nikalte hain
    product *= digit  # Product mein multiply karte hain
    n = n // 10  # Last digit remove karte hain

# Step 4: Product ko print karen
print("Digits ka product hai:", product)
