import sys
input = sys.stdin.readline
queue = []
class q :
    def push_(X) :
        queue.append(X)
    def pop_() :
        if len(queue) < 1 :
            print(-1)
        else :
            print(queue[0])
            del queue[0]
    def size_() :
        print(len(queue))
    def empty_() :
        if len(queue) >= 1 :
            print(0)
        else :
            print(1)
    def front_() :
        if len(queue) < 1 :
            print(-1)
        else :
            print(queue[0])
    def back_() :
        if len(queue) < 1 :
            print(-1)
        else :
            print(queue[-1])
        
N = int(input())
for i in range(N) :
    a = input()
    if a[0] == 'p' and a[1] == 'u':
        num = int((a.split())[1])
        q.push_(num)
    elif a[0] == 'f' :
        q.front_()
    elif a[0] == 'b' :
        q.back_()
    elif a[0] == 'e' :
        q.empty_()
    elif a[0] == 's' :
        q.size_()
    elif a[0] == 'p' :
        q.pop_()
    else :
        print('error')
        
