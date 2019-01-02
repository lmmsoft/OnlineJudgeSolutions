n = int(input())
for i in range(0, n):
    l, r = [int(x) for x in input().split()]
    print("{x} {y}".format(x=l, y=2 * l))
