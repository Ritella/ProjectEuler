# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

max_num = 1000

def main():
    sum_multiples = 0

    for int in range(1, max_num, 1):
        if int % 3 == 0 or (int % 5 == 0):
            sum_multiples += int

    print(str(sum_multiples))

main()


# NOTE: could have done
# not int % 3 and not int % 5, as they evaluate to True
# could have also added to a list using list.append(int)
