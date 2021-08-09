#A問題
a,b = map(int, input().split())

print(max(a+b, a-b, a*b))

#B問題
k,x = map(int, input().split())

s = x-(k-1)
g = x+(k-1)

if s <= -1000000:
  s = -1000000
if g >= 1000000:
  g = 1000000

ans = list(range(s,g+1,1))

print(*ans)

#C問題
import math
import collections
n = int(input())
s = [input() for i in range(n)]

for i in range(n):
  s[i] = ''.join(sorted(s[i]))

c = collections.Counter(s)
d = c.most_common()

l = len(d)
ans = 0

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i in range(l):
  if d[i][1] == 1:
    ans += 0
  else:
    ans += comb(d[i][1],2)

print(ans)
