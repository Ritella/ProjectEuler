# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

# Solution from http://www.s-anand.net/euler.html

r = range(1,101)
squared_sums = sum(r)**2
sum_of_squared = sum([i**2 for i in r])
print(squared_sums- sum_of_squared)
