import sys
N = int(sys.stdin.readline())
A, Pa, B, Pb = map(int,sys.stdin.readline().split())
max_power = 0
power = 0
max_tanker = 0
max_dealer = 0
dealer = 0
for i in range((N // Pa)+1) :
    dealer = ((N-(Pa*i)) // Pb)
    power = (A * i) + (B * dealer)
    if power > max_power :
        max_power = power
        max_tanker = i
        max_dealer = dealer
print(max_tanker, max_dealer)
