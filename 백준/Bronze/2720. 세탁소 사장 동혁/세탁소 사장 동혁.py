Q = 25
D = 10
N = 5
P = 1
T = int(input())
for i in range(T) :
    x = int(input())
    QQ = x // Q
    DD = (x - Q*QQ) // D
    NN = (x - Q*QQ - D*DD) // N
    PP = (x - Q*QQ - D*DD - N*NN) // P
    print(QQ,DD,NN,PP)
