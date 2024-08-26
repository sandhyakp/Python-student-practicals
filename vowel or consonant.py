# Step 1: Alphabet ko input karen
charcter = input("Koi bhi alphabet daaliye: ")

# Step 2: Vowel ya consonant check karen
if charcter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print(charcter, "vowel hai.")
else:
    print(charcter, "consonant hai.")
