def binomial(n, m):
    # terminale
    if m == 0 or m == n:
        return 1
    # non terminale
    else:
        return (binomial(n-1, m-1) +
                binomial(n-1, m))


if __name__ == '__main__':
    n = 6
    m = 3
    print(binomial(n, m))