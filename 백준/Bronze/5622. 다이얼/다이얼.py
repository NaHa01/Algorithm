#5622
a = input()
x = []
for i in range(len(a)) :
    if a[i] == 'A' or a[i] == 'B' or a[i] == 'C' :
        x.append(2)
    elif a[i] == 'D' or a[i] == 'E' or a[i] == 'F' :
        x.append(3)
    elif a[i] == 'G' or a[i] == 'H' or a[i] == 'I' :
        x.append(4)
    elif a[i] == 'J' or a[i] == 'K' or a[i] == 'L' :
        x.append(5)
    elif a[i] == 'M' or a[i] == 'N' or a[i] == 'O' :
        x.append(6)
    elif a[i] == 'P' or a[i] == 'Q' or a[i] == 'R' or a[i] == 'S' :
        x.append(7)
    elif a[i] == 'T' or a[i] == 'U' or a[i] == 'V' :
        x.append(8)
    elif a[i] == 'W' or a[i] == 'X' or a[i] == 'Y' or a[i] == 'Z' :
        x.append(9)
last_num = 0
result = 0
for i in x :
    result += i+1
print(result)