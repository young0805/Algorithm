def traverse(node, tree, order_type):
    if node == '.':
        return ""
    result = []
    if order_type == 'pre':
        result.append(node)
    result.extend(traverse(tree[node][0], tree, order_type))  # 왼쪽 자식
    if order_type == 'in':
        result.append(node)
    result.extend(traverse(tree[node][1], tree, order_type))  # 오른쪽 자식
    if order_type == 'post':
        result.append(node)
    return ''.join(result)

def main():
    N = int(input())  # 노드의 개수
    tree = {}

    for _ in range(N):
        node, left, right = input().split()
        tree[node] = (left, right)

    # 순회 결과 출력
    print(traverse('A', tree, 'pre'))
    print(traverse('A', tree, 'in'))
    print(traverse('A', tree, 'post'))

if __name__ == "__main__":
    main()
