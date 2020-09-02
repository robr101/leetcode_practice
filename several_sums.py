def sums (n: int) -> str:
    k = 1 # int
    while n % 10 ^ k != 0:
        k = n % 100 - (n % 10)
        print (k)