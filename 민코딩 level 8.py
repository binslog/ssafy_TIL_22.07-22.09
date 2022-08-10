# 8-1
# a = 0
# N = int(input())
# while a<N:
#     a = a+1
#     print(a,end=' ')

#------------------------------------------------

# 8-2
# arr = list(map(int,input().split()))
# result=[]

# for i in range(len(arr)) :
#     if arr[i] != 7 :
#         result.append(arr[i])
#     else:
#         break

# result = ' '.join(map(str,result))
# print(result)

#-----------------------------------------------------

# 8-3

# def output_func(n1,n2):
#     num = 5
    
#     while num <= n1 + n2 :    
#         print(num,end='')

# def input_func():
#     n1,n2 = map(int,input().split())
#     return n1,n2
    

# print(input_func)






# 8-4
# arr = list(map(int,input().split()))
# result=[]

# for i in reversed(range(len(arr))) :
#     if arr[i] != 7 :
#         result.append(arr[i])
#     elif arr[i] == 7 :
#         result.append(7)
#         break

# result = ' '.join(map(str,result))
# print(result)

# -------------------------------------------------

# 8-5

# while True :
#         a = 3     
#         print(a,end=' ')

#         a = a+1        
#         print(a,end=' ')
        
#         a = a-3        
#         print(a,end=' ')
        
#         a = a+5        
#         print(a,end=' ')

#         a = a+1
#         print(a,end=' ')
        
#         a = a-2
#         print(a,end=' ')
#         break

# _____________
# 8-6
# 3x4 전적 배열 만들고
# arr = [[0] * 4 for _ in range(3)]

# def input_func():
#     n = int(input())
#     for i in range(3):        
#         for j in range(4):
#             arr[j][i] += (4*i+2) + j
    
#     return arr
#     #arr 배열을 행우선 순회하면서 n부터 채우기

# def process():
#     for i in range(4):
#         for j in range(3):
#             arr[i][j] += 1
#     # arr에 1씩 더하기

# def output_func():
    
#     print(process)    
    
#     # 2차배열 값 출력하기

#-----------------
# 8-8
# arrs = ['#','_','#','_','#','#']
# result=[]
# for arr in arrs :
#     if arr == '#' :
#         print("샵",end='')
#     else:
#         print("무",end='')

#--------------------------

# 8-10
# arr =[[4,3,1,1],[3,1,2,1],[0,0,1,2]]
# num = int(input())
# cnt = 0

# for i in range(len(arr)):
#     for j in range(len(arr[i])):

#         if num == arr[i][j]:
#             cnt += 1
#         else:
#             cnt += 0

# print(f'{cnt}개 존재합니다')







