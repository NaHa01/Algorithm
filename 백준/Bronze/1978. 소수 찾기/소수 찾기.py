N = int(input())
a = list(map(int, input().split()))
q = 1
x = 0
for i in a :
  #print(i)
  if i == 1 :
    continue
  for j in range(2, i) :
    #print(i,":",i % j)
    if i % j == 0 :
      #print(i, "는 소수가 아니었습니다!")
      q = 11
      break
  if q == 11 :
    q = 1
    continue
  else :
    #print(x)
    x += 1   
print(x)