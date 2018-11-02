# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

def get_sum(n):
    return sum([x**x for x in range(1,n+1)])

def get_last_n_digs(num, n_digs):
    str_num = str(num)
    last_n_digs_str = str_num[-n_digs:]
    last_n_digs = int(last_n_digs_str)
    return last_n_digs

def main():
    max_num = 1000
    num_digs = 10
    series_sum = get_sum(max_num)
    last_ten_digs = get_last_n_digs(series_sum, num_digs)
    print(last_ten_digs)

if __name__ == '__main__':
    main()
