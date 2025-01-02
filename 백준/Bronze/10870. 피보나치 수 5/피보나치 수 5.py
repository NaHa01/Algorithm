n = int(input())
bbefore_n = 0
before_n = 1
result = bbefore_n + before_n
for i in range(n-1) :
    result = bbefore_n + before_n
    bbefore_n = before_n
    before_n = result
if n == 0 :
    print(0)
else :
    print(result)