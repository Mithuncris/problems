a = input().lower()
b = input().lower()
for i in range(len(a)):
    if ord(a[i]) < ord(b[i]):
        print(-1)
        break
    elif ord(a[i]) > ord(b[i]):
        print(1)
        break
else:
    print(0)