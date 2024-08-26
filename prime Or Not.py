'''A prime number is a whole number greater
than 1 whose only factors are 1 and itself.
The first ten primes are
2, 3, 5,7, 11, 13, 17, 19, 23, 29.
It should be noted that 1 is a non-prime number.'''

# Step 1: Number input karen
n = int(input("Kisi number ko daliye: "))

# Step 2: Prime flag ko initialize karen
is_prime = True

# Step 3: Loop 2 se lekar sqrt(n) tak chale (basic optimization)
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Agar divisible hai toh prime nahi hai
            is_prime = False
            break
else:
    is_prime = False  # 1 aur usse chhote numbers prime nahi hote

# Step 4: Check karen aur output den
if is_prime:
    print(n, "ek prime number hai.")
else:
    print(n, "ek prime number nahi hai.")
