n=input()
a=[input() for _ in[0]*n]
s={0}
for x in a:s={(y+x)%360for y in s}|{(y-x)%360for y in s}
print'NYOE S'[0in s::2]