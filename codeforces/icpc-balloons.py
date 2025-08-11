for _ in range(int(input())):
    n = int(input())
    l = input()
    ans = 0
    v = set()
    for i in l:
        if i in v:
            ans +=1
        else:
            ans +=2
        v.add(i)
    
    print(ans)