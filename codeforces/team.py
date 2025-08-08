ans = 0
for _ in range(int(input())):
    know = list(map(int, input().split()))
    count = know.count(1)
    if count >=2:
        ans +=1
print(ans)