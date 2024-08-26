# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Last digit find karen
last_digit = n % 10  # Modulo 10 se last digit milti hai

# Step 3: First digit find karne ke liye loop chalate hain
while n >= 10:
    n = n // 10  # Number ko 10 se divide karte hain, taaki first digit last bachi rahe

# Step 4: First digit n mein bachi hoti hai
first_digit = n

# Step 5: Pehli aur aakhri digit ko print karen
print("Pehli digit hai:", first_digit)
print("Aakhri digit hai:", last_digit)
