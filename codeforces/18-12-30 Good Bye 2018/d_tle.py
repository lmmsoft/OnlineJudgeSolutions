import itertools

n = int(input())

# s = "".join(str(i) for i in range(1, n + 1))
s = [i for i in range(1, n + 1)]

l = list(itertools.permutations(s, n))

# print(l)

# ll = sum(l,[])


ll = [item for sublist in l for item in sublist]

# print(ll)

Sum = int(n * (n + 1) / 2)

cnt = 0
for i in range(0, len(ll) - n + 1):
    l2 = ll[i: i + n]
    if sum(l2) == Sum:
        cnt += 1
#
print(cnt % 998244353)
