# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b
# are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

max_num = 10000

divisors = [[] for _ in range(max_num)]  # to initialize a list of lists

for i in range(1, max_num // 2 + 1):  # inner loop defunct at 2i = max_num
    for j in range(i+i, max_num, i):
        divisors[j].append(i) # i is a proper divisor of all n*i numbers

sums = [sum(x) for x in divisors]

ami = 0
for i in range(1, max_num):
    if sums[i] < max_num and i == sums[sums[i]] and i != sums[i]:
        ami += i # don't add the other one yet or you'll overcount

print(ami)


# NOTE: look at how i initialized a list of lists.
# To initialize an empty list you need to have [0]*n or it won't work
# the point is that what's in between the [] is the datatype each list
# element will have. if you just do []*n there's no datatype
# Note also that [[]] * n gives the same list object as each element in the
# overall list, so any modification to 1 list-- i.e. list[i].append(x)--
# will perform that modification all list elements
# i guess this is because the datatype [] is mutable so all reference same
# object, whereas the datatype 0 isn't so you re-assign each value
# Note how I had to write max_num // 2 (not evaluated as a float)
# Also had to do a check on index values because you can't evaluate outside the
# index
# Note that when i first wrote this, I overcounted the amicable sums
# by adding them both each time I found a pair
