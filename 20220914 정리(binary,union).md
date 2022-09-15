> binary search tree 
```python

arr=[0]*20
lst=[4,2,9,7,15,1,3]


def insert(target):
    now=1
    while(1):
        if arr[now]==0:
            arr[now]=target
            return
        if arr[now]<target: now=now*2+1
        else: now=now*2

def search(target):
    now=1
    while 1:
        if now >= 20: return 0  # 배열범위 벗어날 경우
        if arr[now]==0: return 0 # 찾고자 하는 값이 없을경우
        if arr[now]==target: return 1 # 찾았을경우
        if arr[now]<target: now=now*2+1
        else: now=now*2

for i in range(len(lst)):
    insert(lst[i])  # arr배열(트리)에 값 저장하는 함수


n=int(input())   # 숫자 하나 입력받고
answer=search(n)    # 입력받은 숫자가 존재하는지 search하는 함수
if answer: print("존재")
else: print("없는숫자")
```

___

> union find 자료구조
```python
# union find 자료구조
# 각각의 독립되 data를 그룹화 시켜 자료들을 관리할때 사용하는 자료구조

arr=[0]*200


def findboss(member):
    global arr
    if arr[ord(member)]==0: # 매개변수에 해당하는 곳의 값이 0이라면
        return member       # 자기 자신이 보스!!
    ret=findboss(arr[ord(member)]) # 배열에 적혀있는 값으로 다시 보스 찾아보기
    return ret

def union(a,b):
    global arr
    aboss=findboss(a)  # boss 찾기
    bboss=findboss(b)
    if aboss==bboss:  # boss가 같다 -> 이미 같은 그룹
        return
    arr[ord(bboss)]=aboss  # 두보스가 다르다면 b의 보스에 해당하는 값에 a의 보스적기


union('A','B') # 두 그룹을 하나의 그룹으로
union('D','E') # 합쳐주는 함수
union('B','E')
union('B','D')
union('F','E')

y,x=input().split()
if findboss(y)==findboss(x):
    print("같은그룹")
else: print("다른그룹")

```
