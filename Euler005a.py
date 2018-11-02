# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

# Solution from http://www.s-anand.net/euler.html

def gcd(a,b):
    return b and gcd(b, a%b) or a

def lcm(a,b):
    return a * b / gcd(a,b)

def main():
    n = 1
    for i in range(1,21):
        n = lcm(n, i)

    return n

print(main())
