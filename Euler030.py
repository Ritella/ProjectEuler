# Surprisingly there are only three numbers that can be
# written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the
# sum of fifth powers of their digits.

# SOLUTION: if n is the number of digits, the maximum 5th power sum
# that can be written is n * 9^5
# Therefore, find n such that (n) * (9^5) < 10^n - 1
# n can't be more than 6


max_num = 10**6

power_summands = []
for i in range(1, max_num):
    str_i = str(i)
    sum_d = 0
    for d in str_i:
        sum_d += int(d)**5
    if sum_d == i and len(str_i) != 1: power_summands.append(i)

print(sum(power_summands))


# NOTE: cannot name a variable 'sum' or python gets confused since the
# sum object takes precedence over the sum function
