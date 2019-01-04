a = input()
b = [x for x in input().split()]

a1 = a[0]
a2 = a[1]

str = "NO"
for x in b:
    x1 = x[0]
    x2 = x[1]
    if a1 == x1 or a2 == x2:
        str = "YES"
        break
print(str)
