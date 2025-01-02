brackets = input().strip()

stack = []
piece_count = 0

for i, char in enumerate(brackets):
    if char == '(':
        stack.append(char)
    else:  # char == ')'
        stack.pop()
        if brackets[i - 1] == '(': 
            piece_count += len(stack)
        else:  
            piece_count += 1

print(piece_count)
