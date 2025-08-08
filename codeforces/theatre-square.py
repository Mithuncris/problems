import math
n, m, a = map(int, input().split())
v1 = math.ceil(n / a)
v2 = math.ceil(m / a)
print(v1*v2)