n = int(input())
n_before = 1
n_bbefore = 1
n_recent = 2
temp = 0
for i in range(n-2) :
    n_bbefore = n_before
    n_before = n_recent
    n_recent = n_bbefore + n_before
    #print(n_bbefore,n_before,n_recent)
if n == 1 :
    print(4)
else :
    print(n_before*4 + n_bbefore*2)