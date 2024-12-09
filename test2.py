#関数とdictionary

def ave(a, b, c):
  sum = 0
  sum = a + b + c
  result = sum / 3
  return result

def addInfo(name, num):
  price[name] = num
  print(price)
  


price = {
  "PRS":110000,
  "Squier":30000,
  "LesPaul":150000
}

prs = price.get("PRS")
print(prs)
print(price)

#addInfo(input("商品名:"), int(input("価格:")))

x = price.keys()          #dict_keys型  
y = list(price.keys())    #リスト型 
print(x)
print(y)

x_v = price.values()
y_v = list(price.values())
print(x_v)
print(y_v)

for name, values in price.items():
  print(f"{name}の値段は{values}です")



average = ave(9, 4, 2)
print("平均値" + str(average))