import sys
input = sys.stdin.readline
a = []
for i in range(100) :
    x = input().strip('\n')
    a.append(x)
for j in range(100) :
    print(a[j])
