#A問題
a = int(input())
s = input()

if a >= 3200:
  print(s)
else :
  print('red')

#B問題
n = int(input())
a = list(map(int, input().split()))

l = len(a)
s = 0

for i in range(l):
  s += 1 / a[i]

print(1/s)

#C問題
