# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?


def main():
    max_num = 20
    prime_factors = {2:2}

    for int in range(3,max_num+1):
        is_prime = 1
        for prime in prime_factors:
            this_primes_multiples = 0
            while int % prime == 0:
                is_prime = 0
                this_primes_multiples += 1
                int = int/prime
            else:
                prime_factors[prime] = max(prime_factors[prime],
                                           this_primes_multiples)
        else:
            if is_prime:
                prime_factors[int] = 1

    primes = prime_factors.keys()
    multiples = prime_factors.values()

    lcm_factors = list(map(lambda x,y: x**y, primes, multiples))

    lcm = 1
    for factor in lcm_factors:
        lcm *= factor

    return lcm

print(main())


# NOTE: you cant loop through ints (have to loop through primes)
# or you won't account for primes
