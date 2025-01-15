import sys
N, M = map(int,sys.stdin.readline().split())
x = []
for i in range(1,N+1) :
    x.append(i)
temp = 0
a = 0
b = 0
for j in range(M) :
    a, b = map(int,sys.stdin.readline().split())
    temp = x[a-1]
    x[a-1] = x[b-1]
    x[b-1] = temp
for k in range(N) :
    print(x[k], end = ' ')