# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors
# is less than n and it is called abundant if this sum  exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two
# abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be
# written as the sum of two abundant numbers.


def find_divs(div_list):
    for i in range(1, int(len(div_list) / 2 + 1) ):
        for j in range(i + i, len(div_list), i):
            div_list[j].append(i)
    return div_list

def find_abundant(div_list):
    is_abundant_list = [ 1 if sum(y) > x else 0 for x, y in enumerate(div_list)]
    return is_abundant_list

def find_sum_abundants(is_abundant_list):
    is_abundant_summand = [0] * len(is_abundant_list)
    for i in range(2, len(is_abundant_list)):
        a = is_abundant_list[1 : i]
        b = is_abundant_list[i - 1 : 0: -1]
        is_abundant_summand[i] = sum([x*y for x,y in zip(a,b)])
		# is_abundant_summand[i] = sum(list(map(lambda: x, y: x*y, a, b)))
    return is_abundant_summand

def main():
    max = 28124
    divs = [ [] for _ in range(0, max) ]
    divs = find_divs(divs)
    is_abundant = find_abundant(divs)
    is_sum_abundant = find_sum_abundants(is_abundant)
    not_sum_abundants = [x if y == 0 else 0 for x, y in enumerate(is_sum_abundant)]
    return sum(not_sum_abundants)

print(main())

# NOTE:
# Pay attention to ordering of list comprehension if-else statements
# Needed to re-cast as int here: for i in range(1, int(len(div_list) / 2 + 1) )
# Also, for reverse as [::-1] you need to list end-idx first
