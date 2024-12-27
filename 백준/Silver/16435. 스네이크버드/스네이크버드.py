# 스네이크버드의 초기 길이 l과 과일 높이 heights를 입력받아 최대로 증가할 수 있는 스네이크버드의 길이를 반환하는 함수.
def max_snakebird_length(l, heights):
    # 과일 높이를 오름차순으로 정렬
    heights.sort()

    for h in heights:
        if l >= h:
            l += 1  
        else:
            break  
            
    return l


n, l = map(int, input().split())  
heights = list(map(int, input().split()))  


# 함수 호출 및 결과 출력
print(max_snakebird_length(l, heights))
