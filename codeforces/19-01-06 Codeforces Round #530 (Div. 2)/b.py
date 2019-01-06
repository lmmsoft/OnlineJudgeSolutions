import math

n = int(input())

s = math.sqrt(n)
a = int(s)

if a ** 2 == n:
    r = 2 * a
elif a * (a + 1) >= n:
    r = a + a + 1
else:
    r = a + a + 2

print(r)