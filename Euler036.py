# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base,
# may not include leading zeros.)


def dec_to_bin(dec_num):
    bin_num = []
    while dec_num != 0:
        bin_num.insert(0, dec_num % 2)
        dec_num = dec_num // 2
    bin_num = int(''.join([str(x) for x in bin_num]))
    return bin_num

def is_pal(num):
    str_num = str(num)
    is_pal_bool = (list(str_num) == list(str_num[::-1]))
    return is_pal_bool

def main():
    max_num = 10**6
    pal_sum = sum([i for i in range(1, max_num) \
                    if is_pal(i) and is_pal(dec_to_bin(i))])
    print(pal_sum)

if __name__ == '__main__':
    main()


# NOTE:
# list(str_num) == list(str_num).reverse() doesn't work because
# reverse doesn't give you back anything
# similarly, b = list(str_num).reverse() doesn't assign anything
