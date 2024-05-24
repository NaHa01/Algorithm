num = int(input())
for i in range(2000):
    for j in range(2000):
    	if ((3*i) + (5*j)) == num:
            print(i+j)
            quit()
print(-1)
