# https://www.geeksforgeeks.org/tabulation-vs-memoization/


maxn = 100
factorials = [0 for i in range(1, maxn)]

factorials[0] = 1
for i in range(1, maxn - 1):
    factorials[i] = factorials[i-1] * i

for i, factorial in enumerate(factorials):
    print(str(i) + ":" + str(factorial))