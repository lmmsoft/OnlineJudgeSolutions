a, b, c = [int(x) for x in input().split()]

aa = a * 3 + 3
bb = b * 3
cc = c * 3 - 3
print(min(aa, min(bb, cc)))
