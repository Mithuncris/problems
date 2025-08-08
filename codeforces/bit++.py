ans = 0
for _ in range(int(input())):
    s = input()
    if '+' in s:
        ans +=1
    else:
        ans -= 1
print(ans)