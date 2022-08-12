# 8-1
# a = 0
# N = int(input())
# while a<N:
#     a = a+1
#     print(a,end=' ')

#--------------------------------------------------------------- 

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

#-----------------------------------------------------------------

# 8-3
# def input_func():
#     n1,n2 = map(int, input().split())
#     return n1,n2
    
# def output_func(n1,n2):
#     num = 5

#     while num <= n1 + n2:
#         print(num, end = ' ')
#         num += 1

# call_input = input_func()
# # print(call_input)

# n1, n2 = call_input
# # print(n1, n2)

# call_output = output_func(n1, n2)
# call_output


#----------------------------------------------------------------

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

# --------------------------------------------------------------

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


# -------------------------------------------------------------

# 8-6
# arr = [[0] * 4 for _ in range(3)]

# #arr 배열을 행우선 순회하면서 n부터 채우기
# def input_func():
#     n = int(input())
#     for i in range(3):        
#         for j in range(4):
#             arr[i][j] += (4*i+n) + j
    
#     return arr

# call_input = input_func()
# # print(call_input)


# #arr에 1씩 더하기
# def process():
#     for i in range(3):
#         for j in range(4):
#             arr[i][j] += 1
#     return arr

# call_process = process()
# # print(call_input2)            


# # 2차원 배열 출력하기
# def output_func():
    
#     return call_process 
    
# call_output = output_func()


# for i in range(len(call_output)):
#     print(*(call_output[i]))

# ------------------------------------------------------------
# 8-7
# arr = [['B','D','5','Q','A'], ['Q','E','R','E','F']]

# def input_func() :
#     x = str(input())
#     return x

# call_input = input_func()


# def output_func(x) :
#     if x.islower() == True :
#         print(''.join(arr[0]))
#     elif x.isupper() == True :
#         print(''.join(arr[1]))
#     elif x.isdigit() == True : 
#         print("HGFEDCBA")


# call_output = output_func(call_input)

#------------------------------------------------------------


# 8-8
# arrs = ['#','_','#','_','#','#']
# result=[]
# for arr in arrs :
#     if arr == '#' :
#         print("샵",end='')
#     else:
#         print("무",end='')

#-----------------------------------

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


#---------------------------------------------------
# 8-11
#-----------------------------------------------
# arr = [[0] * 3 for _ in range(2)]

# def input_func() :
#     num = list(map(int,input().split()))

#     index=0
#     for i in range(2):
#         for j in range(3):
#             arr[i][j]=num[index]
#             index+=1
#     return arr

# call_input = input_func()
# # print(call_input)

# def process():
#     result = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             result += arr[i][j]

#     return result

# call_process = process()
# # print(call_process)

# def output(process):

#     print(process())

# call_output = output(process)

# call_output






