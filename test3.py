#クラス

class Guitar:
  def __init__(self, name):   #コンストラクタ
    self.name = name

  def sum(self, guitar, option, pick):
    return guitar + option + pick
  
a01 = Guitar("PRS")
sum = a01.sum(int(input("ギター本体:")), int(input("オプション:")), int(input("ピック:")))

outputText = f"{a01.name}をはじめとした商品の合計金額は{sum}となります"
print(outputText)