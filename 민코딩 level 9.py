# 민코딩 level9
#--------------------------------------- 
# 9-1 
# arrs = [4,3,6,1,3,1,5,3]
# n = int(input())
# cnt = 0

# for arr in arrs :
#     if arr == n :
#         cnt += 1

# print(f'숫자{n}개수는{cnt}개')


#------------------------------------------
# 9-2
# arr = [['A','B','C','D','E'],['E','A','B','A','B'],['A','C','D','E','R']]
# a = input()
# cnt = 0


# for i in range(len(arr)) :
#     for j in range(len(arr[i])):
#         if 'a' == arr[i][j] :
#             cnt += 1
        
#         else:
#             cnt += 0

# if cnt >=3 :
#     print("대발견")
# elif cnt >= 1 :
#     print("발견")
# else:
#     print("미발견")

#----------------------------------------------
# 9-3
# arrs = ['A','F','G','A','B','C']
# a,b = map(str,input().split())
# cnt1 = 0
# cnt2 = 0

# for arr in arrs :
#     if a == arr :
#         cnt1 += 1
        
#     elif b == arr :
#         cnt2 += 1

#     else:
#         continue
            

# if cnt1 > 0 and cnt2 > 0 :
#     print("와2개")

# elif cnt1 == 0 and cnt2 == 0 :
#     print("우0개")

# else:
#     print("오1개")

#------------------------------------------
# 9-4
# arr = [3,4,2,5,7,9]
# a,b = map(int,input().split())

# arr[a],arr[b] = arr[b], arr[a]

# print(*arr)

#--------------------------------------------------------

# 9-6

# arr = [[0] * 3 for _ in range(3)]
# num = [list(map(int,input().split())) for _ in range(2)]

# index=65

# for i in range(3) :
#      for j in range(3) :
#         arr[i][j] = chr(index)     
#         index += 1


# x = arr[num[0][0]][num[0][1]]
# y = arr[num[1][0]][num[1][1]]

# x,y = y,x

# arr[num[0][0]][num[0][1]] = x
# arr[num[1][0]][num[1][1]] = y

# for row in arr :
#     print(*row, sep='')

#---------------------------------------------------------
# # 9-7
# arr = [list(map(int,input().split())) for _ in range(6)]
# cnt = 0

# for i in range(6) :
#     if arr[i][0] < arr[i][1] :
#         arr[i][0],arr[i][1] = arr[i][1],arr[i][0] 
#         cnt +=1


# for row in arr:
#     print(*row)

# print(f'{cnt}명')

#----------------------------------------------------------