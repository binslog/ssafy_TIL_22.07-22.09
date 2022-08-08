t = int(input())
for tc in range(1,t+1):
    N = int(input())
    arr = list(map(int,input().split()))

    #c
    c = [0] * 101 # 최대높이 100까지 인덱스 확보
    result = [0] * N # 정렬 전 배열과 같은 크기 배열

    # 카운트 배열
    for i in range(N):
        c[arr[i]] += 1

    # 카운트 누적
    for j in range(1,101) :
        c[j] += c[j-1]

    # 정렬
    for i in range(N-1, -1, -1):
        c[arr[i]] -= 1
        result[c[arr[i]]] = arr[i]

    print(result)