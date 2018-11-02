# An irrational decimal fraction is created by concatenating
# the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part,
# find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def make_irrational_num(max_dig):
    irrational_num = [str(0)]
    i = 1
    num_digs = 1
    while num_digs <= max_dig:
        str_i = str(i)
        irrational_num.append(str_i)
        num_digs += len(str_i)
        i += 1
    return ''.join(irrational_num)

def main():
    irr_num = make_irrational_num(10**6)
    d_prod = 1
    for i in range(0,7):
        d_prod *= int(irr_num[10**i])
    print(d_prod)

if __name__ == '__main__':
    main()


# NOTE:
# only string list can be joined as str
# remember that in line 28, str values have to be recast in order to multiply
