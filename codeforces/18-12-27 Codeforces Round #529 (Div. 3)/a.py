#from sys import stdin, stdout

n = int(input())
s = input()

r=[]
index =0
step =1
while True:
    r.append(s[index:index+1])
    index +=step
    step+=1
    if index >= n:
        break
print(''.join(r))
    