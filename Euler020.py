# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def fact(n):
    if n != 1:
        return n * fact(n-1)
    else:
        return 1

fact_100 = fact(100)
fact_100_list = [int(x) for x in str(fact_100)]
print(sum(fact_100_list))




# NOTE:
# fact_100 (an int) is not iterable
# in order to use sum for digits, you need to recast to list (not str)
