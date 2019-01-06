w, h = [int(x) for x in input().split()]
u1, d1 = [int(x) for x in input().split()]
u2, d2 = [int(x) for x in input().split()]

if d2 > d1:
    u1, u2, d1, d2 = u2, u1, d2, d1

s1 = (h + d1) * (h - d1 + 1) // 2
x = max(0, w + s1 - u1)

s2 = (d2 + d1 - 1) * (d1 - d2) // 2
x = max(0, x + s2 - u2)

s3 = d2 * (d2 - 1) // 2
print(x + s3)

'''
4 6
1 2
1 4
'''
