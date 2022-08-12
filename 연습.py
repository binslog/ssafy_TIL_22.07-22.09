
arr =[[4,7,1,8],[5,5,9,2],[5,9,5,9],[1,2,9,7]]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# location =[(i,j) for i in range(4) for j in range(4) if arr[i][j]==5]




result = 0 # 결과 값 산출 

for i in range(4):
    for j in range(4):
        
        result += arr[x + dx[i]][y + dy[i]] # dx[0] 부터 이차원 배열에 접근!



print(result)












