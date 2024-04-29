x = input()
rx = ''
for i in range(len(x)) :
  rx = rx + x[-i - 1]
if x == rx :
  print(1)
else :
  print(0)