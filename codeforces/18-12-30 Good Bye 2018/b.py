n = int(input())

a1 = 100000000
b1 = 100000000
a2 = -100000000
b2 = -100000000
for i in range(0, n):
    a, b = [int(x) for x in input().split()]
    if a < a1:
        a1 = a
        b1 = b
    if a == a1:
        b1 = min(b, b1)
for i in range(0, n):
    a, b = [int(x) for x in input().split()]
    if a > a2:
        a2 = a
        b2 = b
    if a == a2:
        b2 = max(b, b2)
print("{} {}".format(a1 + a2, b1 + b2))

'''
2
2 1
2 2
3 2
3 1

2
0 0
0 0
1 1
1 1
'''
