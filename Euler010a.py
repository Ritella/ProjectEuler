# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def find_primes(max_num):
    primes = [2]
    all_nums = range(3,max_num,2)
    while len(all_nums) > 0:
        i = all_nums[0]
        primes.append(i)
        all_nums = list(filter(lambda x: x % i != 0, all_nums))
        print('prime number', i)
    return primes

def main():
    max_num = 2000000
    prime_list = find_primes(max_num)
    return sum(prime_list)

print(main())
