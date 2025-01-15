def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_first_n_primes(n):
    count = 0
    num = 2
    primes = []
    while count < n:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1
    print(f"The first {n} prime numbers are: {primes}")

# Input: Number of prime numbers to print
n = int(input("Enter the number of prime numbers to print: "))
print_first_n_primes(n)
