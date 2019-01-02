n = int(input())
s = input()

r = 1
l = len(s)
if l == 1:
    r = 1
elif l == 2:
    r = 3
else:
    a = s[0]
    b = s[-1]

    index = 0
    while True:
        if s[index] == a:
            index += 1
        else:
            break
    la = index

    index = -1
    while True:
        if s[index] == b:
            index -= 1
        else:
            break
    lb = abs(index + 1)

    r = la + lb + 1

    if a == b:
        r += la * lb
    r = r % 998244353

print(r)
