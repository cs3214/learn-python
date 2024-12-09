N = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(0, N):
  minj = i
  
  for j in range(i, N):
    if A[j] < A[minj]: minj = j
    
  A[i], A[minj] = A[minj], A[i]
  if A[i] != A[minj]: count += 1
    
for k in range(N): 
  if k < N-1 :print(A[k], end=" ")
  else: print(A[k])
print(count)
