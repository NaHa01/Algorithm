x = input()
a = ''
n = []
for i in range(len(x)) :
  if ord(x[i]) > 95 :
    n.append(chr(ord(x[i])-32))
  else : 
    n.append(chr(ord(x[i])+32))
a = "".join(n)
print(a)