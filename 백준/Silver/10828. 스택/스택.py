import sys

def main():
    input = sys.stdin.read
    commands = input().splitlines()
    stack = []
    result = []

    # 명령 처리
    for command in commands:
        if command.startswith("push"):
            _, num = command.split()
            stack.append(int(num))
        elif command == "pop":
            result.append(stack.pop() if stack else -1)
        elif command == "size":
            result.append(len(stack))
        elif command == "empty":
            result.append(0 if stack else 1)
        elif command == "top":
            result.append(stack[-1] if stack else -1)

    # 결과 출력
    sys.stdout.write("\n".join(map(str, result)) + "\n")


if __name__ == "__main__":
    main()
