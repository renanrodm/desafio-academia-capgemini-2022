def escada(n):
    for cont in range(1, n+1):
        n = n - 1
        print(' ' * n + "*" * cont)


n = 6
escada(n)
