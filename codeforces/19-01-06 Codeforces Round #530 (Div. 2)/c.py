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
