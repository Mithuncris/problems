for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    first = float('-inf')
    second = float('-inf')
    for i in range(n):
      if l[i]>first:
        second = first
        first = l[i]
      elif l[i]>second:
          second = l[i]
    for i in range(n):
        if l[i]==first:
            ans = second
        else:
            ans = first
        print(l[i]-ans, end=' ')
    print()