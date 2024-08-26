# Step 1: n ka value input karen
n = int(input("n ka value daaliye: "))

# Step 2: Sum ko initialize karen
sum = 0

# Step 3: Loop use karke 1 se n tak ke numbers ka sum calculate karen
for i in range(1, n + 1):
    sum += i  # sum = sum + i

# Step 4: Sum ko print karen
print("1 se", n, "tak ke natural numbers ka sum hai:", sum)
