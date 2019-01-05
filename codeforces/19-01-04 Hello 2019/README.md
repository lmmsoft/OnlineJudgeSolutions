# Contest

- [Link](https://codeforces.com/contest/1097)
- [Official blog](https://codeforces.com/blog/entry/64251)
- [Official Editorial](https://codeforces.com/blog/entry/64310)

## My status
- A: 6 min 1 AC
- B: 13 min 1 AC
- C: 1h6min, TLE first then AC, a unsuccessful hack by others
- D: read problem, have no idea, also don't understand the 2nd sample

## Short code

### A
- 简单的模拟题
- 我的比赛提交，比较啰嗦
```python
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
```
- 可以稍微优化
```python
a = input()
b = [x for x in input().split()]

str = "NO"
for x in b:
    if a[0] == x[0] or a[1] == x[1]:
        str = "YES"
        break
print(str)
```
- 比较短的提交
- 非常巧妙
    - 利用输入元组直接省掉了 a[0]和a[b]的判断
    - 因为字母和数字不重复，可以直接用in判断所有字符不用 第一位第二位分开比较
    - 输出也很巧妙，用了下标访问，False是0，True是1
```python
a, b = input()
c = input()
print(('NO','YES')[a in c or b in c])
```

### B
- 输入n个数，每个数可正可负，求总和会不会等于0或360的倍数
- 暴力枚举即可
- 我的比赛代码
```python
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
```
- 赛后简化之后的代码
```python
n = int(input())
l = [0]
for _ in range(0, n):
    a = int(input())
    l2 = []
    for x in l:
        l2.extend(([x + a, x - a]))
    l = l2

print(("NO", "YES")[any([x % 360 == 0 for x in l])])

```
- 网上的短码，python2
- 非常巧妙
    - 集合从{0}开始，避免空集的特判
    - 用了dict{}的交集 | 运算，合并 y+x与y-x，比list的extend()运算短
    - 输出用了 print'NYOE S'[0 in s::2]，意思是 0 in s 可为True和False，步长是2，取子串
```python
n=input()
a=[input() for _ in[0]*n]
s={0}
for x in a:s={(y+x)%360for y in s}|{(y-x)%360for y in s}
print'NYOE S'[0in s::2]
```

### C
对于每个字符串，可以计算(a,b), a和b分别是添加a个')'和b个'('之后变成correct
- 我的比赛提交
- 写得不好，计算a和b时没能一个循环算出，把字符串逆序之后算了两次
- 统计数字的时候没考虑效率，TLE了一次
```python
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

```

- 赛后优化，根据官方题解，重写一下，更加清晰
```python
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

```