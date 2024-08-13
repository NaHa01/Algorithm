import sys
case = int(sys.stdin.readline())
for i in range(1, case+1):
    a,b = map(int,sys.stdin.readline().split())
    print("Case #", i, ": ", a + b, sep = "") 
