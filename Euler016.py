# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# 2^1000 = (2^15)^200/3

# a = 32768
# b = a**(200/3) # this gives you an inexact amount due to approximations of
                 # square root
a = 2**5
b = a**(200)
print(b)
b_str = str(int(round(b)))
b_int_list = [int(i) for i in b_str]
print(len(b_int_list))
print(sum(b_int_list))

# Note:
# if you write a**200/3, this is evaluated as (a**200)/3
# because exp takes precedence over div operator
# you need to round because square root is approximate
