A,B,V = map(int, input().split())

if (V-B) % (A-B) == 0 :
    print((V-B) // (A-B))
else :
    print(((V-B) // (A-B)) +1)

'''
참고 할 내용
/	나누기
//	나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
%	나누기 연산 후 몫이 아닌 나머지를 구함
'''
