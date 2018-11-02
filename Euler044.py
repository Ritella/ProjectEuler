# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
# The first ten pentagonal numbers are:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
# However, their difference, 70 − 22 = 48, is not pentagonal.

# Find the pair of pentagonal numbers, Pj and Pk, for which their
# sum and difference are pentagonal and D = |Pk − Pj| is minimised;
# what is the value of D?

def pent(n):
    return (n * (3 * n - 1) )/ 2

def make_pent_list(max_num):
    pent_list = [pent(n) for n in range(1,max_num+1)]
    return pent_list

def pent_compare(pent_list):
    for i in pent_list:
        for j in pent_list[pent_list.index(i)-1::-1]:
            if i - j in pent_list and i + j in pent_list:
                    return i - j

def main():
    max_pent = 4000
    pent_list = make_pent_list(max_pent)
    print(pent_compare(pent_list))


if __name__ == '__main__':
    main()


# NOTE:
# Don't forget to use brackets for lists!
# Syntax to check for value is "in"
# main clause uses "name" and "if"
# can't name variables the same as objects
