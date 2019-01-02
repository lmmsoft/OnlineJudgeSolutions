n =int(input())

min1 = 10000000
min2 = 10000000

max1 =0
max2 =0

li = [int(x) for x in input().split()]

for a in li:
    if a < min2:
        min2 = a
        if min2< min1:
            min1,min2 = min2, min1
    
    if a>max2:
        max2 =a
        if max2 > max1:
            max1,max2 = max2,max1

print( min (max2-min1,max1-min2 ))