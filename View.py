T = 10 #int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0 # 조망권 수
    for i in range(2,N-2) : # 조망권 확인 위치
        # h = max(arr[i-2], arr[i-1], arr[i+1}, arr[i+2]) # max를 쓴다면
        h = 0
        for j in range(i-2, i+3): # 주변 4개 중 최대 높이
            if i != j :
                if h < arr[j] :
                    h = arr[j]

        if arr[i] > h : # 주변 4개보다 높으면
            cnt += arr[i] - h # 높이차 만큼 조망권 확보
        print(f'#{tc} {cnt}')
