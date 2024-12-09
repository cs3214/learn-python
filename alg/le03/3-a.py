def push(x):  
  S.append(x)
  
def pop():
  return S.pop()
  
i = 0
A = list(map(str, input().split()))
S = []

for i in range(len(A)):
  if A[i] == "+": push(pop() + pop())
  elif A[i] == "-":push((-1 *pop()) + pop())
  elif A[i] == "*" : push(pop() * pop())

  else: push(int(A[i]))
  
print(S[-1])