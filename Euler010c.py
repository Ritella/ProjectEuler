# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def find_primes(max_num):
    all_nums = range(3,max_num,2)
    all_nums_bool = True * (max_num - 3 + 1)/2
    for i, num in enumerate(all_nums):
        all_nums_bool = [False for x in all_nums_bool if x in range(i,max_num,i)]
    return primes

def main():
    max_num = 2000000
    prime_list = find_primes(max_num)
    return sum(prime_list)

print(main())
