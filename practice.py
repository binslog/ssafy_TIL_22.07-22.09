name=list(input().split())  # B A C D
arr=[
    [0,0,1,1],
    [1,0,1,0],
    [1,0,0,1],
    [0,0,0,0],
]
used=[0]*4
cnt=0
def dfs(now):
    global cnt
    if now==3:
        cnt+=1
    for i in range(4):
        if arr[now][i]==1 and used[i]==0:
            used[i]=1
            dfs(i)
            used[i]=0


used[1]=1
dfs(1)
print(cnt)