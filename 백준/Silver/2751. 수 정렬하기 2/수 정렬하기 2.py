import sys
n = int(sys.stdin.readline().strip())
x=[]
for i in range(n) :
    x.append(int(sys.stdin.readline().strip()))
x.sort()
for j in x :
    print(j)
