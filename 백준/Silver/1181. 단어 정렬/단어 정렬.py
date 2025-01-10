import sys

N = int(sys.stdin.readline())
words = []
small = 0
x = ''
for i in range(N) :
    x = sys.stdin.readline().strip()
    if x in words :
        continue
    else :
        words.append(x)
words.sort(key= lambda word : (len(word), word))
for i in words :
    print(i)