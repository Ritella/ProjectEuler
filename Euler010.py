# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


# NOTE: This runs but is very very slow

def find_primes(max_num):
    primes = [2]
    for i in range(3,max_num,2):
        assumed_prime = 1
        for prime_num in primes:
            if i % prime_num == 0:
                assumed_prime = 0
                break
        if assumed_prime == 1:
            primes.append(i)
    return primes

def main():
    max_num = 2000000
    prime_list = find_primes(max_num)
    return sum(prime_list)

print(main())
