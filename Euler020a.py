# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# Alternative solution from http://www.s-anand.net/euler.html

def digits(n):
    s = 0
    while n > 0:
        s = s + (n % 10)
        n = n / 10
    return s

n = 1
for i in range(1,100): n = n*i
print(digits(n))


# NOTE: can just iterate through numbers to get factorial of a number
# also, keep in mind that repeated num % 10 is a good way to get digits
# out of a number if you can't recast to string or list
