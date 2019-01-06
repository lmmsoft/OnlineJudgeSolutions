# Contest

- [Link](https://codeforces.com/contest/1099)
- [Official blog](https://codeforces.com/blog/entry/64296)
- [Official Editorial(part English part Russian, need translator)](https://codeforces.com/blog/entry/64310)

## My status
- A: 33 min 3 AC
    - 1WA 12min: 没仔细看题，太着急速写了，匆匆过了样例就提交
    - 2WA 26min: 考虑漏了落到地的情况，不应该
- B: 13 min 1 AC
- C: 1h6min, TLE first then AC, a unsuccessful hack by others
- D: read problem, have no idea, also don't understand the 2nd sample
- rating: -18 1447->1429

## Short code

### A 雪球
- 简单的模拟题，雪球落下，每米会增加值为高度的重量，撞到两个石头会减小石头的重量，求最终重量
- 我的比赛提交，用了O(1)的算法，直接等差数列求和了
- 看了大家速写代码，用的O(n)算法，比较好写，不用比较d1 d2大小，也不用推等差数列求和公式
```python
w, h = [int(x) for x in input().split()]
u1, d1 = [int(x) for x in input().split()]
u2, d2 = [int(x) for x in input().split()]

if d2 > d1:
    u1, u2, d1, d2 = u2, u1, d2, d1

s1 = (h + d1) * (h - d1 + 1) // 2
x = max(0, w + s1 - u1)

s2 = (d2 + d1 - 1) * (d1 - d2) // 2
x = max(0, x + s2 - u2)

s3 = d2 * (d2 - 1) // 2
print(x + s3)
```

### B 矩形面积
- 输入形状的面积n，问最小周长
- 很显然是 sqrt(n)附近的值
- 我的比赛代码O(1)，枚举了 floor(sqrt(n)) 和 ceil(sqrt(n)) 前后的三个数字，找到最小值
- 看了网上写的比较快的代码 很多都是O(n) , 让ans从0开始递增，算 (ans/2) * (ans-ans/2) >= n，找到ans
- 其他看到的O(1)代码和我的思路差不多
```python
import math

n = int(input())

s = math.sqrt(n)
a = int(s)

if a ** 2 == n:
    r = 2 * a
elif a * (a + 1) >= n:
    r = a + a + 1
else:
    r = a + a + 2

print(r)
```
- 看了比较短的python代码，有些技巧
    - import math 的 sqrt 代码比较长，可以直接 n ** 0.5

```python
import math
print(math.ceil(2*math.sqrt(int(input()))))
```

```python
print(1+int((4*int(input())-3)**0.5))
```

### C
- 字符串模拟题
    - ? 可以让字符串长度不变，也可以减1
    - *可以加n,不变，减一
    - 那么最终的长度范围是 len(string) 为去除? * 之后的字符串长度
        - when len(*)=0 :  [len(string) - len(?), len(string)]
        - when len(*) !=0 : [len(string) - len(?) - len(*) , + INF)
    - 长度在范围之外就是 Impossible
    - 长度在范围之内就模拟拼凑一下， special judge, 仔细处理一下就好

- 我的比赛提交
    - 写得不算太好
    - 统计?和*的个数可以用 str.count('?')，不需要枚举
    - str.find()可以找下标
```python
s = input()
k = int(input())

a = 0
b = 0
bindex = -1
ss = ""

for i in range(0, len(s)):
    if s[i] is '?':
        a += 1
    elif s[i] is '*':
        b += 1
        bindex = i

l = len(s) - a - b
lmin = l - a - b
if k < lmin or (k > l and b == 0):
    print("Impossible")
else:
    if l - k < 0:
        # use * for k -l times
        ss = s[0:bindex - 1] + s[bindex - 1] * (k - l + 1) + s[bindex + 1:]

    elif l - k == 0:
        ss = s
    elif l - k > 0:
        # l-k = a1+b1 => use a first ,then use b
        if l - k <= a:
            # a enough, (l-k) a
            cnt = l - k
            i = len(s) - 1
            lc = []
            while i >= 0:
                if s[i] == '?' and cnt > 0:
                    i -= 1
                    cnt -= 1
                else:
                    lc.append(s[i])
                i -= 1
            ss = ''.join(lc)[::-1]
        else:
            # a and (l-k-a) b
            cnt = l - k - a
            i = len(s) - 1
            lc = []
            while i >= 0:
                if s[i] == '?':
                    i -= 1
                elif s[i] == "*" and cnt > 0:
                    i -= 1
                    cnt -= 1
                else:
                    lc.append(s[i])
                i -= 1
            ss = ''.join(lc)[::-1]
    lc = []
    for c in ss:
        if c not in ['?', '*']:
            lc.append(c)
    print(''.join(lc))

'''
a?b*c
6

a?b*c
3

a?b*c
2

a?b*b*c
2

'''


```

- 赛后优化，根据别人比较短的代码，添加注释
```python
s = input()
k = int(input())
n = s.count('*')
m = s.count('?')
l = len(s) - m - n
if k < l - m - n or (n == 0 and k > l):
    s = 'Impossible'
elif k > l:
    # 需要添加 k-l 个 *前面的数字
    # 用replace('*'，个数，1) 把第一个*替换为k-l个前面的字母即可
    i = s.find('*')
    s = s.replace('*', s[i - 1] * (k - l), 1)
# 下面一行很巧妙，处理删l-k个字符的时候，直接吧*换成?，避免判断?和*个数的情况
s = s.replace('*', '?')
# 类似于 in range(0, l-k)， 如果l-k小于等于0的话是不循环的
for _ in [0] * (l - k):
    i = s.find('?')
    # 删除 ?和前面的字符，拼起来一起replace with ''
    s = s.replace(s[i - 1] + '?', '', 1)
print(s.replace('?', ''))
```