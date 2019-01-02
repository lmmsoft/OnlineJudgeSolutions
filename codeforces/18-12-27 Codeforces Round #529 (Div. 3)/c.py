n, k = [int(x) for x in input().split()]

li = []
s = {}
s2 = {}
num = 1
while True:
    s[num, 1] = [num]
    li.append(num)
    num *= 2
    if num > n:
        break

for index in range(2, k+1):
    for a, ai in s.keys():
        for l in li:
            sum = l + a
            if sum <= n and not s.get((sum, index)):
                s2[sum, index] = s.get((a, index-1)).append(l)
    s = s2

if s.get(n,k):
    print("YES")
    string = " ".join(s.get((n,k)))
    print(string)
else:
    print("NO")
