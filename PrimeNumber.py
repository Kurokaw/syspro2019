n = 10000
while True:
    for p in range(2, n):
        if n % p == 0:
            break
    print(str(n))
    n = n + 1