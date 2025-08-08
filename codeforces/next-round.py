n, k = map(int, input().split())
a = list(map(int, input().split()))
place = a[k-1] if a[k-1]>0 else 0
ans = 0
for i in range(n):
    if a[i] >= place and a[i]>0:
        ans += 1
    else:
        break
print(ans)