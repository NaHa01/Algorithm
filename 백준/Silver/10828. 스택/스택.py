import sys

N = int(sys.stdin.readline())
N_list = []

for i in range(N) :
    a = sys.stdin.readline()
    if a[0:2] == 'pu' :
        a_split = a.split(' ')
        a_num = a_split[-1]
        N_list.append(a_num)
    elif a[0:2] == 'po' :
        if len(N_list) == 0 :
            print(-1)
        else :
            N_list_pop = N_list.pop()
            print(N_list_pop, end = '')
    elif a[0:2] == 'si' :
        print(len(N_list))
    elif a[0:2] == 'em' :
        if len(N_list) == 0 :
            print(1)
        else :
            print(0)
    else :
        if len(N_list) == 0 :
            print(-1)
        else :
            print(N_list[-1], end = '')