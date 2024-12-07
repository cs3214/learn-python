#変数　条件文　繰り返し文　リスト
print('Hello World')
print("Good morning")

num1 = 1
num2 = 20
num3 = 20

string_a = "アゴツマガツチ"

bool_a = (num1 > num2)

#リスト
list_a = ["ララ", "クラッシュ", "アゴツ", "マガツチ", "参上"]

print("変数の中身は" + str(num1))
print("変数の中身は" + string_a)
print("変数の中身は" + str(bool_a))
print("変数の中身は" + str(list_a[num1]))

print(num1 > num2 and num2 >= num3)
print(num1 > num2 or num2 >= num3)

for i in range(10):
  if i == len(list_a) : break
  elif i == 2: continue
  print(list_a[i])

print(list_a[2:5])

