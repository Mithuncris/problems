n, q = map(int, input().split())
a = list(map(int, input().split()))

diff = [0] * (n + 1)
for _ in range(q):
    l, r = map(int, input().split())
    l-=1
    r-=1
    diff[l] += 1
    diff[r+1] -= 1

freq = [0]*n
freq[0] = diff[0]
for i in range(1,n):
    freq[i] = freq[i-1] + diff[i]    
freq.sort()
a.sort()
max_sum = sum(f*v for f, v in zip(freq, a))
print(max_sum)