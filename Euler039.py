# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?


def find_pythagorean_solns(max_num):
    num_solns = [0] * (max_num + 1)
    for a in range(1, max_num):
        for b in range(1, a+1):
            c = (a**2 + b**2)**(0.5)
            if c % 1 == 0:
                p = int(a + b + c)
                if p <= max_num:
                    num_solns[p] += 1
    max_p = num_solns.index(max(num_solns))
    return max_p

def main():
    max_num = 1000
    print(find_pythagorean_solns(max_num))

if __name__ == '__main__':
    main()

# NOTE:
# Need to recast floats to ints in order to use as indices
# Be careful with maxing out ranges
# fucntions need parentheses
