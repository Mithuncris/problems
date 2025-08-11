n, m = map(int, input().split())
l = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
s = set()
for i in range(n-1, -1, -1):
    if l[i] in s:
        ans = 0
    else:
        s.add(l[i])
        ans = 1
    prefix_sum[i] = prefix_sum[i + 1] + ans
for _ in range(m):
    x = int(input())
    print(prefix_sum[x-1])