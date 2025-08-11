for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
    
    for _ in range(q):
        left, right, k = map(int, input().split())
        left-=1
        right-=1
        original_range_sum = prefix_sum[right+1] - prefix_sum[left]
        new_range_sum = k * (right - left + 1)
        

        query_sum = prefix_sum[n] - original_range_sum + new_range_sum
        
        print("YES" if query_sum % 2 == 1 else "NO")