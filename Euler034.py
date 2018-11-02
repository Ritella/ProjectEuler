# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the
# sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# Solution: n * 9! < 10^n - 1 when n = 7

from math import *

def fact():
    factorial_list = []
    for i in range(0, 10):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        factorial_list.append(factorial)
    return factorial_list

def fact_sum_digits(num):
    global fact_list
    fact_sum = sum([fact_list[int(x)] for x in list(str(num))])
    return fact_sum

def find_curious_nums(max_num):
    curious_num_sum = sum([x for x in range(3,max_num) \
                        if fact_sum_digits(x) == x])
    return curious_num_sum

def main():
    max_num = fact_list[9]*7
    print(find_curious_nums(max_num))

fact_list = fact() # no need to call fact every time since only 10 possible vals

if __name__ == '__main__':
    main()

# NOTE:
# dicts support by-index assignment
# lists support by-index modification but not assignment
# tuples and strings support neither (immutable)
# to change a str do str[0:i] + 's' + str[i+1:]
# to add to a tuple do tup = ();
# tup = tup + (value,)
# you need the , in the second parameter to distinguish it as a tuple
# rather than an int
