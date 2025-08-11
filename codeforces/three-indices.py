for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    found = False
    for j in range(1, n-1):
        if a[j-1] < a[j] and a[j] > a[j+1]:
            print("YES")
            print(j, j+1, j+2)
            found = True
            break
    if not found:
        print("NO")