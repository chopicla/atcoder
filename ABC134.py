#A問題
a = int(input())
print(3*a*a)

#B問題
n,d = map(int, input().split())

a = d * 2 + 1

if n < a:
  print(1)
else:
  if n % a == 0:
    print(int(n/a))
  else:
    print(int(n/a)+1)

#C問題
n = int(input())
a = [int(input()) for i in range(n)]
ma = max(a)
num = len(a)
ans = 0

for i in range(num):
  if a[i] == ma:
    ans += 1

for i in range(num):
  if ans == 1:
    if a[i] != ma:
      print(ma)
    else:
      a.sort(reverse = True)
      print(a[1])
  else:
    print(ma)
