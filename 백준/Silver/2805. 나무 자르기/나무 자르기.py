import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

min_ = 0  
max_ = max(tree)  

def check(height):
    sum_trees = 0
    for i in tree:
        if i > height:
            sum_trees += i - height
    return sum_trees

while min_ <= max_:
    mid = (max_ + min_) // 2
    trees = check(mid)
    if trees < M:
        max_ = mid - 1
    elif trees > M:
        min_ = mid + 1
    else :
        max_ = mid
        break

print(max_)