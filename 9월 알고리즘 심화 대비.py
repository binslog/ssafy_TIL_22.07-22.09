# 1.
#
# arr=[[0,0,0,0,0],
#      [0,1,3,1,0],
#      [0,3,0,3,0],
#      [0,1,3,1,0],
#      [0,0,0,0,0]]
#
#
# directy=[1,-1,0,0] # 아래 위 왼 오
# directx=[0,0,-1,1]
# cnt = 0 # 개수 세야된다
#
#
# def find_bomb(y,x):
#     global cnt
#     for i in range(4):
#         for m in range(1,5):
#             dy=y+directy[i]*m
#             dx=x+directx[i]*m
#             if dy<0 or dy>4 or dx<0 or dx>4: break # 배열을 벗어났거나 m방향 안가도 된다,,,
#             if arr[dy][dx] == 3: break # 벽을 만나면 m의 방향만큼 갈 이유는 없다
#             if arr[dy][dx] == 0: # 만약 0이면...
#                 arr[dy][dx]=4
#
#     return
#
#
# # 다 돌아야된다.
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] == 1:
#             find_bomb(i,j)
#
#
# # 마지막에 출력해준다.
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] ==0:
#             cnt+=1
#
# print(cnt)

# ----

# # arr=[
# #     [0, 0, 3, 0, 0],
# #     [0, 3, 1, 0, 3],
# #     [0, 3, 1, 0, 3],
# #     [3, 0, 0, 1, 0],
# #     [0, 3, 1, 0, 3],
# # ]
# ## answer : 6
# arr = [[0, 0, 0, 0, 0],
#        [0, 1, 3, 1, 0],
#        [0, 3, 0, 3, 0],
#        [0, 1, 3, 1, 0],
#        [0, 0, 0, 0, 0]]
#
# ## answer : 9
# N = 5
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# matrix = [[1] * N for _ in range(N)]
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] == 3:
#             matrix[i][j] = 0
#         if arr[i][j] == 1:
#             for k in range(4):
#                 tx, ty = i, j
#                 while 0 <= tx < 5 and 0 <= ty < 5 and arr[tx][ty] != 3:
#                     matrix[tx][ty] = 0
#                     tx += dx[k]
#                     ty += dy[k]
# print(sum([sum(v) for v in matrix]))

# ------------------------------------------------------------------

# 2














# --------------------------
# 3. MST, 크루스칼 : 서술형
