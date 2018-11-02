# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1,1001):
    for b in range(1,a+1):
        c = (a**2 + b**2)**0.5
        if (c % 1 == 0) and (a + b + c == 1000):
            print(a*b*c)
