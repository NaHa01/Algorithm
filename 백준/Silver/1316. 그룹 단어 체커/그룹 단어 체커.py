N = int(input())
N_not = 0
check = 1
for i in range(N) : # 입력 받을 횟수
    if check == 0 :
        #print("check is 0")
        check = 1
        N_not += 1
        #print("N_not", N_not)
    #print(check)
    a = input()
    for j in range(len(a)) :# 입력받은 문자열의 길이만큼 반복
        for k in range(j + 1, len(a)) : #입력받은 문장열에서 해당 문자가 언제까지 반복되는지 확인
            if a[k] != a[j] : # 입력받은 문자열이 연속해서 나오지 않는다는 것 확인
                #print("문자열이 연속하지 않는다는 것을 확인함.", a[k], a[j])
                for l in range(k, len(a)) : # 연속해서 나오지 않다가 갑자기 같은 문자가 다시 나오면 끝남
                    if a[l] == a[j] : # 그러다가 같은 단어가 나오면 check를 false
                        #print("같은 단어가 나옴",a[l], a[j])
                        check = 0
                        #print(check)
if check == 0 :
        #print("check is 0")
        check = 1
        N_not += 1
        #print("N_not", N_not)

print(N - N_not)
