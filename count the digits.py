# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Digit count karne ke liye counter ko initialize karen
count = 0

# Step 3: Loop tab tak chale jab tak number 0 nahi ho jaata
while n > 0:
    n = n // 10  # Number ko 10 se divide karte jaate hain, last digit remove hoti hai
    count += 1  # Har baar count badhata hai

# Step 4: Digit count ko print karen
print("Digits ki total ginti hai:", count)
