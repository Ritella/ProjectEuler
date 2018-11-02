def fib(dict,n):
    if n not in dict:
        dict[n] = fib(dict,n-1) + fib(dict, n-2)
    return dict[n]

def main():
    dict = {1:1, 2:1}
    print(fib(dict, 10))

if __name__ == '__main__':
    main()
