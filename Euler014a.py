# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# Solution from http://www.s-anand.net/euler.html


def collatz(num, cache):
    if not num in cache:  # alternatively, if not cache.get(n,0)
        if num % 2 == 0: cache[num] = 1 + collatz(num / 2, cache)
        else: cache[num] = 1 + collatz(3 * num + 1, cache)
    return cache[num]

def main():
    cache = {1:1}
    chain_size = [0] * 1000000
    n,c = 0,0
    for i in range(1,1000000):
        cache[i] = collatz(i,cache)
        #print('collatz', i, 'is', cache[i])
        if cache[i] > c: n,c = i,cache[i]
    return n

print(main())
