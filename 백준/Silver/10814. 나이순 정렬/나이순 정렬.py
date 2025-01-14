import sys
n = int(sys.stdin.readline().strip())
x = []
a = 0
b = ''
c = []
for i in range(n):
    a,b = sys.stdin.readline().split()
    c  = [int(a), i, b]
    x.append(c)
x.sort()
for i in range(n) :
    print(x[i][0], x[i][2])
