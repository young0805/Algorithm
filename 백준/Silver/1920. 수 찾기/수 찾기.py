def main():
    N = int(input()) 
    arr = set(map(int, input().split())) 

    M = int(input())  
    queries = list(map(int, input().split()))  

    for query in queries:
        if query in arr:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()
