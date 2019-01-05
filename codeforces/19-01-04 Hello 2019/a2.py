a = input()
b = [x for x in input().split()]

str = "NO"
for x in b:
    if a[0] == x[0] or a[1] == x[1]:
        str = "YES"
        break
print(str)
