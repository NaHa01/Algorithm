aa = int(input())
N = 1000 - aa
count = 0;

count += N // 500
N = N % 500
    #print(N)

count += N // 100
N = N % 100
    #print(N)

count += N // 50
N = N % 50
    #print(N)

count += N // 10
N = N % 10
    #print(N)

count += N // 5
N = N % 5
    #print(N)

count += N // 1
    #print(N)
print(count)