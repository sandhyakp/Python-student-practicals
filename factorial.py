# Step 1: Number input karen
n = int(input("Kisi number ka factorial nikalne ke liye number daaliye: "))

# Step 2: Factorial ko initialize karen
factorial = 1

# Step 3: Loop use karke factorial calculate karen
for i in range(1, n + 1):
    factorial *= i  # factorial = factorial * i

# Step 4: Factorial ko print karen
print("Factorial of", n, "hai:", factorial)
