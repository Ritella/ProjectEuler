# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order.

# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the
# digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

digs = [0,1,2,3,4,5,6,7,8,9]

order_num = 1000000

n = len(digs)

perm_value = []

while len(digs) > 0:
    fact_n = 1
    for i in range(1,n): fact_n *= i
    if order_num % fact_n == 0:
        idx = int((order_num / fact_n) - 1)
    else:
        idx = int(order_num // fact_n)
    order_num = order_num - idx * fact_n
    dig = digs.pop(idx)
    perm_value.append(str(dig))
    n = len(digs)

print(''.join(perm_value))


# NOTE:
# If you write out the orders of [0,1,2,3] you see that the 4 possible values of
# the first digit rotates every 6 (i.e. 3!) times.
# In other words, 0 repeats 6 times,
# then 1 for 6 numbers, then 2 for 6 numbers, etc.
# Likewise, the 3 possible values of the second digit rotate every 2! times
# Must convert to int in order to use as index.
# Float doesn't work as index
# Must also convert digit to string
# Otherwise, list cannot be recast as str via join
