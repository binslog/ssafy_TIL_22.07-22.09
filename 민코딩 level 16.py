# 레벨 16-1
# words = [input() for _ in range(3)]
# for word in words:
#     print(word[-1],end='')

# 레벨 16-2
# board = [
#     ["A", "B", "K", "T"],
#     ["K", "F", "C", "F"],
#     ["B", "B", "Q", "Q"],
#     ["T", "P", "Z", "F"]
# ]

# alphabet = list(map(str,input().split()))
# cnt =0
# for i in board :
#     for j in range (4) :
#         if i[j] == alphabet[0] :
#             cnt += 1
#         elif i[j] == alphabet[1] :
#             cnt += 1

# print(cnt)


# 레벨 16-3
# word = list(input())
# num = int(input())

# word.insert(num,'A')
# result = ''.join(map(str,word))
# print(result)

# # 레벨 16-4
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
# result =[0]*4

# result[0] = A[0] + B[3]
# result[1] = A[1] + B[2]
# result[2] = A[2] + B[1]
# result[3] = A[3] + B[0]

# for i in range(4) :
#     result[i] = A[i] + B[3-i]

# result = ' '.join(map(str,result))
# result.split()
# print(result)

#----------------------------

# # 16-5
# word = str(input())
# list_word = list(word)
# index = int(input())

# # print(list_word)

# list_word.remove(list_word[index])
# result=''.join(map(str,list_word))
# print(result)

#-----------------------------

# 16-6 
# arr = list(map(int,input().split()))

# for i in range(len(arr)-1):
#     arr[i+1] = arr[i] + arr[i+1]

# result = ' '.join(map(str,arr))
# print(result)

##------------------------------

## 16-7
# words = [input() for _ in range(3)]
# key=0

# for word in words :
#     if 'M' in word :
#         key += 1

#     else:
#         key += 0
    

# if key > 0  :
#     print("M이 존재합니다.")
# else :
#     print("M이 존재하지 않습니다.")

# def put(n):
#   n = int(input())
#   arr = [list(map(int,input())) for _ in range(n)]
#     return arr

# print(arr)