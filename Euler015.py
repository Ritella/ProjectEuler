# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


# Imagine going from (20,20) to (0,0)
# you have to move 40 times, 20 times in each dimension
# ordering of dimensions is up to you
# slotting the 20 x-dimension moves into your 40 moves
# gives you 40 C 20



def fact (n, cache):
    if n not in cache:
        cache[n] = n * fact(n - 1, cache)
    return cache[n]

def main():
    cache = {1:1}
    return fact(40, cache) / (fact(20, cache) * fact(20, cache))

print(main())

# Notes:
# don't forget to call fact with the cache argument
# don't set cache[n] as n * cache[n-1]! That's not recursive!
