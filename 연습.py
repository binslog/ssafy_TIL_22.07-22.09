n = int(input())
candidate = ["A","B","C","D"]
path = [0] * n

def abc(level,candidate):
    if level == n :
        for i in range(level):
            print(path[i],end='  ')
    
    for i in range(4):
        path[level] = candidate[i]
        abc(level+1,candidate)

abc(0,candidate)