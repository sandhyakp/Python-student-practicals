def sum_natural_upto_n():
    n = int(input("Enter a number n: "))
    total_sum = 0
    
    for i in range(1, n+1):
        total_sum += i
    print(f"Sum of natural numbers up to {n} is: {total_sum}")


sum_natural_upto_n()
