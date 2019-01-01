n = int(input())

d = {}

nn = n
for i in range(2, n + 1):
    if i > nn:
        break
    while nn % i == 0:
        nn = nn / i
        d[i] = d.get(i, 0) + 1

l = len(d)
num = []
cnt = []
cur = []
for k, v in d.items():
    num.append(k)
    cnt.append(v)
    cur.append(0)

result = []


def cal(n, k):
    cnt = int(n / k + 1)
    return int((1 + n + 1) * cnt / 2 - (n + 1))


def calJi():
    # num cur
    s = 1
    for i in range(0, l):
        s *= pow(num[i], cur[i])
    result.append(s)


def check(index):
    if index == l:
        s = 1
        for c in cur:
            calJi()
            return

    for i in range(0, cnt[index] + 1):
        #  i => 1 to cnt[index]
        cur[index] = i
        check(index + 1)


check(0)

r2 = [cal(n, k) for k in result]
r3 = sorted(r2)

print(" ".join(map(str, r3)))
