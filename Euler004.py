# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def main():
    sorted_three_dig_prods = three_dig_prods()

    pal = largest_pal(sorted_three_dig_prods)

    return pal



def three_dig_prods():

    sorted_three_dig_prods = []
    min = 100
    max = 1000
    for i in range(min,max):
        for j in range(min,i+1):
            sorted_three_dig_prods.append(i*j)
    sorted_three_dig_prods.sort(reverse=True)
    return sorted_three_dig_prods


def largest_pal(number_list):
    for num in number_list:  # can just iterate over the list
        str_num = str(num)
        if str_num == str_num[::-1]:
            return num
    return 'None'


print(main())


# NOTE:
# remember that behavior is different if you are sorting a list of
# strings or a list of ints.  If a string list of ints-- i.e. '1', '22'
# will go by the value of the first digit, rather than the cardinality

# Note that reverse() is to reverse a list order by index rather than value
