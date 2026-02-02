# Finding Prime: O(sqrt(N))
def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


# Prime Factors (Striver end) : O(sqrt(N) + logN) = O(sqrt(N))
import math
n = int(input())

res = []
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        res.append(i)

        while n%i == 0:
            n = n//i

if n>1:
    res.append(n)
print(res)

'''
Q) Why we use sqrt(n)?


For example:

Take n = 60.
Its factors are: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60.

Notice:

2 pairs with 30,
3 pairs with 20,
4 pairs with 15,
5 pairs with 12.

Once we reach sqrt(60) ≈ 7.7, all pairs have already been found.
'''