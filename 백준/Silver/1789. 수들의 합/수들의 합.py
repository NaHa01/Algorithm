#1789

S = int(input())
result = 0
i_sum = 0

for i in range(1, S+1) :
    if i_sum + 2*i + 1 > S :
        result += 1
        break
    else :
        i_sum += i
        result += 1
        continue
print(result)
