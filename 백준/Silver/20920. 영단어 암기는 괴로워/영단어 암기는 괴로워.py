import sys
from collections import Counter

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
words = data[1:]

# 길이 M 이상 단어 필터링 및 빈도 계산
filtered_words = [word for word in words if len(word) >= M]
word_count = Counter(filtered_words)

# 정렬
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

sys.stdout.write("\n".join(word for word, _ in sorted_words) + "\n")
