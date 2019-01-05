n = int(input())
l = [0]
for _ in range(0, n):
    a = int(input())
    l2 = []
    for x in l:
        l2.extend(([x + a, x - a]))
    l = l2

print(("NO", "YES")[any([x % 360 == 0 for x in l])])
