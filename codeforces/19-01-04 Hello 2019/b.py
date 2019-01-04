n = int(input())

l = []

for i in range(0, n):
    a = int(input())
    if not l:
        l.append(a)
    else:
        l2 = []
        for x in l:
            l2.append(x + a)
            l2.append(x - a)
        l = l2

str = "NO"
for x in l:
    if x % 360 == 0:
        str = "YES"
        break
print(str)
