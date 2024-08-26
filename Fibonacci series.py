# Step 1: Number of terms input karen
n = int(input("Kitne terms chahiye Fibonacci series mein: "))

# Step 2: First two terms initialize karen
a, b = 0, 1

# Step 3: Loop use karke Fibonacci series print karen
print(a)
print(b)
for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c
