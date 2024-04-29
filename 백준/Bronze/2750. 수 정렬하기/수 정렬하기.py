N = int(input())
a = []
x = ''
for i in range(N) :
  x = int(input())
  a.append(x)
a.sort()
for j in range(len(a)) :
  print(a[j])