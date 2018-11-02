# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

def collatz(num, chain_idx):
    if num == 1:
        return chain_idx
    elif num % 2 == 0:
        return collatz(num / 2, chain_idx + 1)
    else:
        return collatz(3 * num + 1, chain_idx + 1)

def main():
    chain_size = [0] * 1000000
    for i in range(1,1000000):
        chain_size[i] = collatz(i,1)
        # print('collatz', i, 'is', chain_size[i])
    return chain_size.index(max(chain_size))

print(main())
