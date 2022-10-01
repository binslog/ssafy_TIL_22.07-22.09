n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

name = [x for x in range(n)] # 받은 숫자로 숫자배열 하나 생성!

answer=[]
def dfs(now):
    global answer
    answer.append(name[now])
    for i in range(n):
        if arr[now][i]==1:
            dfs(i)

dfs(0)  # 0번 인덱스 부터 깊이우선 탐색 시작
print(*answer)