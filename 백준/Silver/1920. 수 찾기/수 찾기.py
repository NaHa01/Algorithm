import sys

N = int(sys.stdin.readline())
A = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
X = sys.stdin.readline().split()

for i in range(M) :
  if X[i] in A :
    print(1)
  else :
    print(0)