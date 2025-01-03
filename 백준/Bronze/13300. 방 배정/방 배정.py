n, k = map(int,input().split())
# 0 = 여자 1 = 남자
x = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
for i in range(n) :
    a, b = map(int,input().split())
    if a == 0 :
        if b == 1:
            x[0][0]+=1
        elif b == 2:
            x[0][1] += 1
        elif b == 3:
            x[0][2] += 1
        elif b == 4:
            x[0][3] += 1
        elif b == 5:
            x[0][4] += 1
        elif b == 6:
            x[0][5] += 1
    elif a == 1 :
        if b == 1:
            x[1][0]+=1
        elif b == 2:
            x[1][1] += 1
        elif b == 3:
            x[1][2] += 1
        elif b == 4:
            x[1][3] += 1
        elif b == 5:
            x[1][4] += 1
        elif b == 6:
            x[1][5] += 1
result = 0
for i in range(2) :
    for j in range(6) :
        if (x[i][j] % k) > 0 :
            result += (x[i][j] // k) + 1
        else :
            result += (x[i][j] // k)
print(result)

    
    
