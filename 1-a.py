N = int(input())
A = list(map(int, input().split()))

for i in range(N):
  v = A[i]
  j = i-1
  while j >= 0 and A[j] > v:
    A[j+1] = A[j]
    j-=1
  A[j+1] = v
  
  for k in range(N):
    if(k < N - 1): print(A[k], end=' ')
    else: print(A[k])