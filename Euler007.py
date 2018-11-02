# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10,001st prime number?

primes = [2]

N_PRIME = 10001

i = 3
while len(primes) < N_PRIME:

    prime_idx = 0
    is_prime = 1
    while prime_idx < len(primes):
        if i % primes[prime_idx] == 0:
            is_prime = 0
            break
        else:
            prime_idx += 1

    if is_prime:
        primes.append(i)

    i += 2

print(primes[N_PRIME-1])
