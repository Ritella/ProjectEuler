# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def main():

    def fib_nums(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fib_nums(n-1) + fib_nums(n-2)

print(main())

# this is a good way to write out the fibonnaci sequence recursively
# but very computationally intensive and need to store somehow and add