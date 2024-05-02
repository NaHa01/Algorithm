N = int(input())
n = str(N)
result = N
not_ = 0

if N < 100 :
    result = N
else :
    for i in range(100, N+1) :
        I = str(i)
        d = int(I[1]) - int(I[0])
        for j in range(1, len(I)) :
            if (int(I[j]) - int(I[j-1])) == d :
                continue
            else :
                not_ += 1
                break

            
print(result - not_)