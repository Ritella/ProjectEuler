# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576.

# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by
# 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where n > 1?


def get_pan_num(num):
    all_digs = '123456789'
    pan_try = ''
    for j in range(1, 10):
        pan_try += str(num*j)
        if len(pan_try) == 9:
            pan_num_sort = ''.join(sorted(list(pan_try)))
            if  pan_num_sort == all_digs:
                return int(pan_try)
            else: return 0
        elif len(pan_try) > 9:
            return 0

def main():
    max_num = 10000

    max_pan_num = 0
    for i in range(9, max_num, 1):
        new_pan_num = get_pan_num(i)
        if new_pan_num > max_pan_num: max_pan_num = new_pan_num
    print(max_pan_num)


if __name__ == "__main__":
    main()
