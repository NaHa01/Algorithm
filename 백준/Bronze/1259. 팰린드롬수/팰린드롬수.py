N = []
RN = []
while True :
  N = list(input())
  if N[0] == '0' :
    break
  #print(N)
  RN = []
  for i in range(len(N)) :
    RN.append(N[-1-i])
    #print(i, RN)
    #print(i, N)
  else :
    if RN == N :
      print('yes')
    else :
      print('no')