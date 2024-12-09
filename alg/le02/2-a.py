flag = 1
count = 0
N = int(input())
A = list(map(int, input().split()))

while flag:
  flag = 0
  for j in range(N-1, 0, -1):
    if A[j] < A[j-1]:
      A[j], A[j-1] = A[j-1], A[j]
      count += 1
      flag = 1
      
for i in range(N):
  if(i < N-1): print(A[i], end=" ")
  else: print(A[i])
  
print(count)      