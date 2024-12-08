word = input()  # 단어 S를 입력받음
alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 알파벳 소문자 리스트

for i in alphabet:  # 알파벳 a부터 z까지 반복
    if i in word:  # 해당 알파벳이 단어에 포함되면
        print(word.index(i), end=' ')  # 해당 알파벳의 첫 번째 등장 위치 출력
    else:
        print(-1, end=' ')  # 해당 알파벳이 단어에 없으면 -1 출력
