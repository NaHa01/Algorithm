import sys

N = int(sys.stdin.readline())
a = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
b = (sys.stdin.readline().split())

for i in b:
    if i in a:
        print(1, end=' ')
    else:
        print(0, end=' ')
