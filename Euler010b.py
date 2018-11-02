# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# solved by http://www.s-anand.net/euler.html

sieve = [True] * 2000000    # Sieve is faster for 2M primes

def mark(sieve, x):
    for i in range(x+x, len(sieve), x):
        sieve[i] = False

for x in range(2, int(len(sieve) ** 0.5) + 1):
     if sieve[x]: mark(sieve, x)

print(sum(i for i in range(2, len(sieve)) if sieve[i]))

# Note the way in which sieve is created
# Note that even though non-primes can exist past max^0.5,
# search for them is no longer necessary because the earliest multiple of
# a prime max^0.5 that is not a multiple of values less than that is
# max^(0.5)* max^(0.5)
# check out the sum function
# This script double-sets values as False if multiple of more than one prime
# Even so, it's still much faster than mine since it sets values of multiples
# whereas mine examines each remaining element for divisibility
# also I think mine may be much slower because of the re-initialization of
# each list
