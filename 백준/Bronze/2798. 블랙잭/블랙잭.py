N, M = map(int, input().split())
x = list(map(int, input().split()))  
result = 0
aa = 0
answer = 0
for i in range(N) :
  for j in range(N) :
    for k in range(N) :
      if i == j or j == k or i == k :
        continue
      aa = (x[i] + x[j] + x[k])
      if aa > result and aa <= M :
        result = aa
        answer = aa
print(answer)