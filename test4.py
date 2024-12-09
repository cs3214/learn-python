def push(x):  
  S.append(x)

  
def pop():
  return S.pop()
  
i = 0
count = -1
A = list(map(str, input("input : ").split()))
S = []
print(A)

for i in range(len(A)):
  if A[i] == "+":
    a = pop()
    b = pop() 
    print(a, b)
  else: push(int(A[i]))
  
print(count)