def vowel():
    alpha = input("Enter an alphabet: ").lower()
    
    if alpha in 'aeiou':
        print(f"{alpha} is a Vowel")
    else:
        print(f"{alpha} is a Consonant")

vowel()
