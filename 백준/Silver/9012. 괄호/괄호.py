import sys

def is_vps(ps):
    balance = 0
    for bracket in ps:
        if bracket == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                return "NO"
    return "YES" if balance == 0 else "NO"

def main():
    input = sys.stdin.read
    lines = input().splitlines()
    t = int(lines[0])
    results = [is_vps(ps) for ps in lines[1:]]
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
