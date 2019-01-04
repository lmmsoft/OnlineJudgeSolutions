def check(s, reverse):
    if not reverse:
        a = "("
        b = ")"
    else:
        a = ")"
        b = "("

    m = 0
    for c in s:
        if m:
            if c == a:
                m += 1
            else:
                m -= 1
        else:
            if c == b:
                return False, 0
            else:
                m += 1
    if not reverse:
        return True, m
    else:
        return True, -m


n = int(input())

l = []
l0 = 0

for i in range(0, n):
    s = input()

    b, m = check(s, False)
    # print(b, m)

    if b == True and m == 0:
        l0 += 1
        continue

    if b == True:
        l.append(m)
        continue

    b, m = check(s[::-1], True)
    # print(b, m)

    if b == True:
        l.append(m)
        continue

num = l0 // 2

# TLE
# ll = sorted(l)
# for i in ll:
#     if i >= 0:
#         break
#
#     if -i in l:
#         l.remove(-i)
#         num += 1

d = {}
for i in l:
    d[i] = d.get(i, 0) + 1

for i in l:
    if d.get(i) and d.get(-i):
        d[i] -= 1
        d[-i] -= 1
        num += 1

print(num)
