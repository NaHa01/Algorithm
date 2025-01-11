import sys
N, B, H, W = map(int,sys.stdin.readline().split())
#N:참가자 수 / B:예산 / H:호텔 수 / W : 주의 개수
x=[]
min_ = 500001
max_wp = 0
for i in range(H) :
    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))
    x.append([a,b])
    #a는 예산 b는 수용 가능 인원
for i in range(H) :
    max_wp = max(x[i][1])
    if N < max_wp and min_> N*x[i][0][0] :
        min_ = N*x[i][0][0]
if min_ == 500001 or min_ > B :
    print("stay home")
else :
    print(min_)
    
    
