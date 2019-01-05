def check(s):
    a = 0
    b = 0
    for c in s:
        if c == "(":
            a += 1
        else:
            a -= 1
        if a < 0:
            b += 1
            a = 0
    return a, b


n = int(input())
d = {}

for i in range(0, n):
    s = input()
    a, b = check(s)
    if a == 0 and b == 0:
        d[0] = d.get(0, 0) + 1
    elif a != 0 and b == 0:
        d[a] = d.get(a, 0) + 1
    elif b != 0 and a == 0:
        d[-b] = d.get(-b, 0) + 1

num = d.get(0, 0) // 2

for i in d:
    if i < 0 and d.get(i) and d.get(-i):
        num += min(d.get(i), d.get(-i))

print(num)
