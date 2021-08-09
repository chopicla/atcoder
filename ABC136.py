#A問題
a,b,c = map(int, input().split())

d = a - b
ans = c - d

if ans >= 0:
  print(ans)
else:
  print(0)

#B問題
n = int(input())
ans = 0
for i in range(1,n+1):
  if len(str(i))%2 == 1:
     ans += 1
print(ans)

#C問題
n = int(input())
h = list(map(int, input().split()))
flag = 1

for i in range(1,n):
  if h[i] - 1 >= h[i-1]:
    h[i] -= 1

k = sorted(h)
if h == k:
  print('Yes')
else:
  print('No')

  
