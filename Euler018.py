# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

test_triangle = [[3], \
                [7, 4], \
                [2, 4, 6], \
                [8, 5, 9, 3]]

triangle = [[75], \
            [95, 64], \
            [17, 47, 82], \
            [18, 35, 87, 10], \
            [20, 4, 82, 47, 65], \
            [19, 1, 23, 75, 3, 34], \
            [88, 2, 77, 73, 7, 63, 67], \
            [99, 65, 4, 28, 6, 16, 70, 92], \
            [41, 41, 26, 56, 83, 40, 80, 70, 33], \
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], \
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], \
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], \
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], \
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], \
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

# As there are only 16384 routes, it is possible to solve this problem
# by trying every route. However, Problem 67, is the same challenge with a
# triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)


# SOLUTION:
# 2^14 possible soltns b/c you can move left or right for each of the 14 rows
# If you think about this from top-down there's no way to solve because you
# might constrain yourself to a path that's worse in the long run
# if you think about it bottom-up, soltn is obvious
# at each junction, it's only ever worth taking the maximum of the two possible
# options, b/c you already know what the options are
# also note that python doesn't accept leading zeros for numbers-- i.e. 04

def get_sum(data, row, column):
    if row == len(data):
        return 0
    else:
        return data[row][column] + \
                max([get_sum(data, row + 1, column), \
                get_sum(data, row + 1, column + 1)])

print(get_sum(triangle, 0, 0))

# NOTE:
# First time I wrote this I made an error by calling "triangle" rather
# than data from within get_sum
# Also, IMPORTANT, is that I initially had
# data[row][column] = data[row][column] + max(...)
# return data
# This led to errors. In recursive functions, cannot change the
# underlying structure. What happened is that data[row][column] would have
# different values depending on whether it had been set already (or not)
# in a prior recursive thread
