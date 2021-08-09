#A問題
a,b = map(int, input().split())
if (a+b) % 2 == 0:
  print(int((a+b)/2))
else:
  print('IMPOSSIBLE')

#B問題
import copy
n = int(input())
p = list(map(int, input().split()))
s = sorted(p)
count = 0

for i in range(n):
  if p[i] != s[i]:
    count += 1

if count == 0 or count == 2:
  print('YES')
else:
  print('NO')

#C問題
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

for i in range(n):
  left = min(a[i],b[i])
  ans += left
  a[i] -= left
  b[i] -= left

  right = min(a[i+1],b[i])
  ans += right
  a[i+1] -= right
  b[i] -= right

print(ans)
