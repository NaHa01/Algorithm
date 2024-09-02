num1 = int(input())
num2 = int(input())
count = 0
check = 0
mini = 0
if num1 == 1 and num2 == 1:
    print(-1)
else :
    for i in range(num1, num2+1) :
        for j in range(2,i) :
            if i % j == 0 :
                check += 1
        if check == 0 :
            if count == 0 :
                mini = i
            count += i
        else :
            check = 0
    if count == 0 :
        print(-1)
    else :
        if num1 == 1 :
            count -= 1
            mini += 1
        print(count)
        print(mini)