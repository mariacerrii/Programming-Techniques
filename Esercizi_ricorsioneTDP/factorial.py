def factorial(n):
    #condizione terminale
    if n == 0 or n == 1:
        return 1
    #condizione non terminale
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    N = 20
    print(factorial(N))