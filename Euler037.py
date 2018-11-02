# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def make_prime_list(max_num):
    prime_list = [1] * max_num
    prime_list[0:2] = [0] * 2  # 0 and 1 aren't primes
    for i in range(2, int(max_num**0.5 + 1)):
        if prime_list[i] == 1:
            for j in range(i+i, max_num, i):
                prime_list[j] = 0
    return prime_list

def check_trunc_prime(n, prime_list):
    str_n = str(n)
    is_trunc_prime = 1
    for i in range(0,2):
        if i == 1: str_n = str_n[::-1]
        for j in range(1, len(str_n)):
            trunc_n = str_n[j:]
            if i == 1: trunc_n = trunc_n[::-1]
            if prime_list[int(trunc_n)] == 0:
                is_trunc_prime = 0
                return is_trunc_prime
    return is_trunc_prime

def main():
    prime_list = make_prime_list(10**7)
    sum = 0
    count = 0
    for i in range(10, len(prime_list)):
        if prime_list[i] == 1 and check_trunc_prime(i, prime_list) == 1:
            sum += i
            count += 1
            print('prime', i)
        if count == 11: break
    print(sum)




if __name__ == '__main__':
    main()
