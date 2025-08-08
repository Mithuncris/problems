ans = ''
vowels = 'AEIOUYaeiouy'
s = input()
for i in s:
    if i in vowels:
        continue
    else:
        ans += '.'
        if i.isupper():
            ans += i.lower()
        else:
            ans += i
print(ans)