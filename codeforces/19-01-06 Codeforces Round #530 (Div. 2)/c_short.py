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